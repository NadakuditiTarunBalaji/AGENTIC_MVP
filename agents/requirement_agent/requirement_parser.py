import re
import json

class RequirementParser:

    def detect_domain(self, requirement):

        requirement = requirement.lower()

        if "battery" in requirement:
            return "Battery"

        elif "motor" in requirement:
            return "Powertrain"

        elif "coolant" in requirement:
            return "Thermal"

        elif "seatbelt" in requirement:
            return "Safety"

        return "Unknown"

    def detect_signal(self, requirement):

        requirement = requirement.lower()

        if "battery" in requirement and "voltage" in requirement:
            return "Battery_Voltage"

        elif "battery" in requirement and "temperature" in requirement:
            return "Battery_Temperature"

        elif "motor" in requirement and "speed" in requirement:
            return "Motor_Speed"

        elif "motor" in requirement and "torque" in requirement:
            return "Motor_Torque"

        return "Unknown"
    

    def detect_calibration(self, requirement):

        requirement = requirement.lower()

        if "battery" in requirement and "voltage" in requirement:
            return "BAT_MAX_VOLTAGE"

        elif "battery" in requirement and "temperature" in requirement:
            return "BAT_MAX_TEMP"

        elif "motor" in requirement and "speed" in requirement:
            return "MAX_MOTOR_SPEED"

        return "Unknown"
    


    def detect_dtc(self, requirement):

        requirement = requirement.lower()

        if "battery" in requirement and "voltage" in requirement:
            return "PB001"

        elif "battery" in requirement and "temperature" in requirement:
            return "PB004"

        elif "motor" in requirement and "speed" in requirement:
            return "PP001"

        return "Unknown"
    

    def detect_fault(self, requirement):

        requirement = requirement.lower()

        if "battery" in requirement and "voltage" in requirement:
            return "FAULT001"

        elif "battery" in requirement and "temperature" in requirement:
            return "FAULT004"

        elif "motor" in requirement and "speed" in requirement:
            return "FAULT016"

        return "Unknown"
    

    def detect_testcase(self, requirement):

        requirement = requirement.lower()

        if "battery" in requirement and "voltage" in requirement:
            return "TC001"

        elif "battery" in requirement and "temperature" in requirement:
            return "TC002"

        elif "motor" in requirement and "speed" in requirement:
            return "TC011"

        return "Unknown"
    
    def detect_parameter(self, requirement):

        requirement = requirement.lower()

        if "battery" in requirement and "voltage" in requirement:
            return "Battery Voltage"

        elif "battery" in requirement and "temperature" in requirement:
            return "Battery Temperature"

        elif "battery" in requirement and "current" in requirement:
            return "Battery Current"

        elif "motor" in requirement and "speed" in requirement:
            return "Motor Speed"

        elif "motor" in requirement and "torque" in requirement:
            return "Motor Torque"

        elif "motor" in requirement and "current" in requirement:
            return "Motor Current"

        elif "motor" in requirement and "voltage" in requirement:
            return "Motor Voltage"

        elif "coolant" in requirement and "temperature" in requirement:
            return "Coolant Temperature"

        elif "seatbelt" in requirement:
            return "Seatbelt Status"

        return "Unknown"

    def parse(self, requirement):

        value_match = re.search(r"\d+", requirement)
        unit_match = re.search(r"\d+\s*([A-Za-z%]+)", requirement)

        return {
                "requirement": requirement,
                "value": value_match.group() if value_match else None,
                "unit": unit_match.group(1) if unit_match else None,
                "domain": self.detect_domain(requirement),
                "signal": self.detect_signal(requirement),
                "calibration": self.detect_calibration(requirement),
                "dtc": self.detect_dtc(requirement),
                "fault": self.detect_fault(requirement),
                "testcase": self.detect_testcase(requirement),
                "parameter": self.detect_parameter(requirement),
}
    



if __name__ == "__main__":

    parser = RequirementParser()

    requirements = [
        "Battery pack voltage shall not exceed 420V during normal operation.",
        "Motor speed shall not exceed 12000 RPM.",
        "Battery temperature shall not exceed 60C."
    ]

    for req in requirements:
        result = parser.parse(req)
        print(json.dumps(result, indent=4))
        print("-" * 50)