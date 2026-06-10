from fastapi import FastAPI, HTTPException, Depends, Query
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from src.models import (
    LeadInput,
    LeadResponse,
    UserRegister,
    RoleUpdate,
    AuditLogResponse
)

from src.database.dependencies import get_db

from src.database.lead_model import Lead

from src.database.user_model import User

from src.database.repository import (
    get_lead_stats,
    get_recent_leads
)

from src.database.user_repository import (
    get_user_by_username
)

from src.database.init_db import (
    init_db
)

from src.services.lead_service import LeadService

from src.exceptions.handlers import (
    global_exception_handler
)

from src.auth.security import (
    create_access_token
)

from src.auth.dependencies import (
    get_current_user
)

from src.auth.passwords import (
    hash_password,
    verify_password
)

from src.auth.rbac import (
    admin_required
)

from src.database.audit_log_model import AuditLog

from src.database.audit_repository import (
    create_audit_log
)

app = FastAPI(
    title="AI Lead Qualification System"
)

init_db()

app.add_exception_handler(
    Exception,
    global_exception_handler
)

# -----------------------------------
# Health Check
# -----------------------------------

@app.get("/")
def health():

    return {
        "status": "healthy",
        "service": "AI Lead Qualification System"
    }


# -----------------------------------
# Authentication
# -----------------------------------

@app.post("/register")
def register(
    user: UserRegister,
    db: Session = Depends(get_db)
):

    existing = get_user_by_username(
        db,
        user.username.strip().lower()
    )

    if existing:

        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    db_user = User(
        username=user.username.strip().lower(),
        password_hash=hash_password(
            user.password
        ),
        role="USER"
    )

    db.add(db_user)

    db.commit()

    db.refresh(db_user)

    create_audit_log(
        db,
        username=db_user.username,
        action="USER_CREATED"
    )

    return {
        "message": "User created successfully"
    }


@app.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    user = get_user_by_username(
        db,
        form_data.username.strip().lower()
    )

    if not user:
        
        create_audit_log(
            db,
            username=form_data.username.strip().lower(),
            action="LOGIN_FAILED"
        )

        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(
        form_data.password,
        user.password_hash
    ):

        create_audit_log(
            db,
            username=form_data.username.strip().lower(),
            action="LOGIN_FAILED"
        )

        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    create_audit_log(
        db,
        username=user.username.strip().lower(),
        action="USER_LOGGED_IN"
    )

    token = create_access_token(
        {
            "sub": user.username.strip().lower(),
            "role": user.role,
            "user_id": user.id
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


@app.get("/me")
def get_me(
    current_user=Depends(get_current_user)
):

    return current_user


# -----------------------------------
# Lead Processing
# -----------------------------------

@app.post(
    "/process",
    response_model=LeadResponse
)
def process_lead(
    input: LeadInput,
    db: Session = Depends(get_db)
):

    return LeadService.process_lead(
        db=db,
        message=input.message.strip()
    )


# -----------------------------------
# Admin - Lead Management
# -----------------------------------

@app.get("/leads")
def get_leads(
    limit: int = Query(default=20, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    db: Session = Depends(get_db),
    admin=Depends(admin_required)
):

    return (
        db.query(Lead).limit(limit).offset(offset).all()
    )


@app.get("/analytics")
def analytics(
    db: Session = Depends(get_db),
    admin=Depends(admin_required)
):

    return get_lead_stats(db)


@app.get("/recent-leads")
def recent_leads(
    limit: int = Query(default=10, ge=1, le=100),
    db: Session = Depends(get_db),
    admin=Depends(admin_required)
):

    return get_recent_leads(
        db=db,
        limit=limit
    )


# -----------------------------------
# Admin - User Management
# -----------------------------------

@app.get("/users")
def get_users(
    limit: int = Query(default=20, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    db: Session = Depends(get_db),
    admin=Depends(admin_required)
):

    users = (
        db.query(User).limit(limit).offset(offset).all()
    )

    return [
        {
            "id": u.id,
            "username": u.username,
            "role": u.role,
            "created_at": u.created_at
        }
        for u in users
    ]


@app.put("/users/{user_id}/role")
def update_user_role(
    user_id: int,
    payload: RoleUpdate,
    db: Session = Depends(get_db),
    admin=Depends(admin_required)
):

    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    
    if user.id == admin["user_id"]:
        raise HTTPException(
            status_code=400,
            detail="Cannot change your own role"
        )

    old_role = user.role

    user.role = payload.role

    db.commit()

    create_audit_log(
        db,
        username=user.username.strip().lower(),
        action=f"ROLE_CHANGED {old_role} -> {payload.role}"
    )

    return {
        "message": f"{user.username} role updated to {payload.role}"
    }


@app.get(
    "/audit-logs",
    response_model=list[AuditLogResponse]
)
def get_audit_logs(
    db: Session = Depends(get_db),
    admin=Depends(admin_required)
):

    return (
        db.query(AuditLog)
        .order_by(
            AuditLog.timestamp.desc()
        )
        .all()
    )