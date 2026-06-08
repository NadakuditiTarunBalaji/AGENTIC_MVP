from backend.repositories.fault_repository import get_fault_by_id

def analyze_fault(db, fault_id):
    fault = get_fault_by_id(db, fault_id)

    if not fault:
        return {
            "error": "Fault not found"
        }

    return {
        "fault_id": fault.fault_id,
        "fault_name": fault.fault_name,
        "severity": fault.severity,
        "root_cause": fault.root_cause,
        "recommendation": generate_recommendation(
            fault.severity,
            fault.root_cause
        )
    }

def generate_recommendation(severity, root_cause):

    if severity == "Critical":
        return "Stop vehicle immediately and inspect system."

    if severity == "High":
        return "Schedule immediate maintenance."

    if severity == "Medium":
        return "Inspect during next service."

    return "Monitor vehicle condition."