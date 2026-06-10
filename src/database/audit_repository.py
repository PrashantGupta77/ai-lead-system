from src.database.audit_log_model import AuditLog


def create_audit_log(
    db,
    username,
    action
):

    log = AuditLog(
        username=username,
        action=action
    )

    db.add(log)

    db.commit()

    return log