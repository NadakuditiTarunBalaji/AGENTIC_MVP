import json
import pandas as pd


class MasterDataManager:

    def __init__(self):

        self.calibration_master = pd.read_excel("data/raw/Calibration_Master.xlsx")

        self.dtc_master = pd.read_excel("data/raw/DTC_Master.xlsx")

        self.fault_master = pd.read_excel("data/raw/Fault_Master.xlsx")

        self.signal_master = pd.read_excel("data/raw/Signal_Master.xlsx")





    def get_calibration_limit(self, parameter_name):

        result = self.calibration_master[
            self.calibration_master["Parameter_Name"] == parameter_name
        ]

        if result.empty:
            return None

        return result.iloc[0]["Value"]
    
    

    
    def get_dtc_by_signal(self, signal):

        result = self.dtc_master[
            self.dtc_master["Related_Signal"] == signal
        ]

        if result.empty:
            return None

        return result.iloc[0]["DTC_Code"]


    def get_fault_by_dtc(self, dtc_code):

        result = self.fault_master[
            self.fault_master["Related_DTC"] == dtc_code
        ]

        if result.empty:
            return None

        return result.iloc[0]["Fault_ID"]


    def get_signal_details(self, signal_name):

        result = self.signal_master[
            self.signal_master["Signal_Name"] == signal_name
        ]

        if result.empty:
            return None

        return {
            "signal_id": result.iloc[0]["Signal_ID"],
            "domain": result.iloc[0]["Domain"],
            "unit": result.iloc[0]["Unit"],
            "source_ecu": result.iloc[0]["Source_ECU"]
        }
    
    def get_calibration_by_signal(self, signal_name):

        result = self.calibration_master[
            self.calibration_master["Related_Signal"] == signal_name
        ]

        if result.empty:
            return None

        return {
            "parameter_name": result.iloc[0]["Parameter_Name"],
            "value": result.iloc[0]["Value"],
            "unit": result.iloc[0]["Unit"]
        }
    

    def get_signal_ecu(self, signal_name):

        result = self.signal_master[
            self.signal_master["Signal_Name"] == signal_name
        ]

        if result.empty:
            return None

        return result.iloc[0]["Source_ECU"]




if __name__ == "__main__":

    manager = MasterDataManager()

    print(
    json.dumps(
        manager.get_calibration_by_signal(
            "Battery_Voltage"
        ),
        indent=4,
        default=str
    )
)