import solaredge_setapp
import solaredge_setapp.maintenance_pb2

import datetime


class Maintenance:
    
    def __init__(self, bytes=False):
        if bytes:
            return self.parse_protobuf(bytes)

    def parse_protobuf(self, bytes):
        
        # str name
        # int utf_offset
        # str ntp_server
        # int timestamp
        # list inverters {
            # str serial
            # dict isolation {int fault_location, int isolation, int alpha}
            # dict optimizers_status {int total, int online}
            # list optimizers {
                # str serial
                # bool online
                # float po_power
                # int po_voltage
                # int module_voltage
                # int module_current
                # int temperature 
                # int timestamp
            # }
        # }

        try:
            proto = solaredge_setapp.maintenance_pb2.Maintenance()
            proto.ParseFromString(bytes)
            
            parsed = {
                "system": str(proto.system.name),
                "utc_offset": int(proto.time.utc_offset.value),
                "ntp_server": str(proto.time.ntp_server.value),
                "timestamp": int(datetime.datetime.strptime(
                    "{year} {month} {day} {hour} {minutes} {seconds}".format(
                    year=proto.time.current_time.year.value,
                    month=proto.time.current_time.month.value,
                    day=proto.time.current_time.day.value,
                    hour=proto.time.current_time.hour.value,
                    minutes=proto.time.current_time.minutes.value,
                    seconds=proto.time.current_time.seconds.value
                ), "%Y %m %d %H %M %S").timestamp()),
                "afci": {
                    "enabled": bool(proto.afci.enabled.value),
                    "manual_reconnect": bool(proto.afci.manual_reconnect.value)
                }
            }

            parsed["inverters"] = []

            for inverter in proto.diagnostics.inverters.primary, proto.diagnostics.inverters.left, proto.diagnostics.inverters.right:
                if inverter.serial:
                    parsed["inverters"].append({
                        "serial": str(inverter.serial.value),
                        "isolation": {
                            "fault_location": int(inverter.isolation.fault_location.value),
                            "isolation": int(inverter.isolation.r_iso.isolation),
                            "alpha": int(inverter.isolation.alpha.isolation)
                        },
                        "optimizers_status": {
                            "total": int(inverter.optimizers_status.total.value),
                            "online": int(inverter.optimizers_status.online.value)
                        },       
                        "optimizers": [{
                            "serial": str(po.serial.value),
                            "online": bool(po.online.value),
                            "po_voltage": int(po.po_voltage.value),
                            "module_voltage": int(po.module_voltage.value),
                            "module_current": int(po.module_current.value),
                            "temperature": int(po.temperature.degrees.value),
                            "timestamp": 0 if not bool(po.online.value) else int(datetime.datetime.strptime(
                                "{year} {month} {day} {hour} {minutes} {seconds}".format(
                                year=po.last_report.year.value,
                                month=po.last_report.month.value,
                                day=po.last_report.day.value,
                                hour=po.last_report.hour.value,
                                minutes=po.last_report.minutes.value,
                                seconds=po.last_report.seconds.value
                            ), "%Y %m %d %H %M %S").timestamp())
                        } for po in inverter.optimizer]
                })
        except AttributeError as e:
            print(f"AttributeError: {e}")

        return parsed
