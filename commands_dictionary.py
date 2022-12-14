production_commands = {
    "01": {"name":"CALIB_CMD_READ_DATA", "description": ""},
    "02": {"name":"CALIB_CMD_WRITE_DATA", "description": ""},
    "03": {"name":"CALIB_CMD_READ_VOLTAGE_CURRENT_RMS", "description": ""},
    "04": {"name":"CALIB_CMD_AUTO_CALIBRATION", "description": ""},
    "05": {"name":"CALIB_CMD_SIGN_PARAMETERS", "description": "put hash and signature in place for measurement parameters."},
    "06": {"name":"CALIB_CMD_HASH_PARAMETERS", "description": "put hash at the at of flash block for parameters."},
    "07": {"name":"CALIB_CMD_FORCE_FW_UPDATE", "description": "force meter reset + fw download."},
    "08": {"name":"CALIB_CMD_TEST_COMM", "description": "Test communication."},
    "09": {"name":"CALIB_CMD_AUTO_CALIBRATION_NEUTRAL", "description": "Neutral current auto calibration"},
    "0a": {"name":"CALIB_CMD_SET_VISIBILITY", "description": "Set the number of visibilities of the meter, use just to reduce the number."},
    "0b": {"name":"CALIB_CMD_READ_DATAFLASH", "description": "Read entire external data flash."},
    "0c": {"name":"CALIB_CMD_SET_TARIFF_MODALITY", "description": "Configure meter as monomial, binomial or normal"},
    "0d": {"name":"CALIB_CMD_TOU_RELOAD", "description": "Command to reload table TOU used when modifying table by writing by memory ID and SubID (manufacture)"},
    "20": {"name":"CALIB_CMD_READ_STACK", "description": "Readout actual stack usage."},
    "21": {"name":"CALIB_CMD_SPEED_UP_LED", "description": "Speed up the metrological led."},
    "22": {"name":"CALIB_CMD_MONITOR_PARAMETERS", "description": "Read and write monitors parameters."},
    "30": {"name":"CALIB_CMD_INT_DATA_FLASH_ERASE_ALL", "description": "Erase meter entire internal flash."},
    "31": {"name":"CALIB_CMD_EXT_DATA_FLASH_ERASE_ALL", "description": "Erase meter entire external flash."},
    "32": {"name":"CALIB_CMD_EXT_DATA_FLASH_ERASE_REGISTER", "description": "Erase meter registers."},
    "33": {"name":"CALIB_CMD_EXT_DATA_FLASH_ERASE_LOG", "description": "Erase meter logs."},
    "34": {"name":"CALIB_CMD_EXT_DATA_FLASH_ERASE_DATA", "description": "Erase meter logs and registers"},
    "40": {"name":"CALIB_CMD_RTC_READ_TIME", "description": "Read time data from RTC."},
    "41": {"name":"CALIB_CMD_RTC_WRITE_TIME", "description": ""},
    "42": {"name":"CALIB_CMD_RTC_ENABLE_1HZ", "description": ""},
    "43": {"name":"CALIB_CMD_RTC_DISABLE_1HZ", "description": ""},
    "44": {"name":"CALIB_CMD_RTC_OFFSET", "description": ""},
    "45": {"name":"CALIB_CMD_TEMPERATURE_OFFSET", "description": ""},
    "46": {"name":"CALIB_CMD_METER_VERIFICATION", "description": ""},
    "47": {"name":"CALIB_CMD_METER_VERIFICATION_DATA", "description": ""},
    "48": {"name":"CALIB_CMD_METER_VERIFICATION_HASH", "description": ""},
    "49": {"name":"CALIB_CMD_METER_VERIFICATION_SIGNATURE", "description": ""},
    "50": {"name":"CALIB_CMD_CHANGE_UART_SPEED", "description": ""},
    "51": {"name":"CALIB_CMD_START_TRACE", "description": ""},
    "52": {"name":"CALIB_CMD_STOP_TRACE", "description": ""},
    "53": {"name":"CALIB_CMD_TEST_REGISTER", "description": ""},
    "54": {"name":"CALIB_CMD_TEST_BUTTONS", "description": ""},
    "55": {"name":"CALIB_CMD_TEST_LEDS", "description": ""},
    "56": {"name":"CALIB_CMD_READ_INFO_VERSION", "description": ""},
    "57": {"name":"CALIB_CMD_TEST_SU", "description": ""},
    "58": {"name":"CALIB_CMD_TEST_DISPLAY", "description": ""},
    "59": {"name":"CALIB_CMD_TEST_MAG_SENSOR", "description": ""},
    "5a": {"name":"CALIB_CMD_TEST_INTERFACES_PINS", "description": ""},
    "5b": {"name":"CALIB_CMD_READ_INFO_GRIDSTREAM", "description": ""},
    "5c": {"name":"CALIB_CMD_TEST_DISCONNECTOR", "description": ""},
    "5d": {"name":"CALIB_CMD_EMUL_MEASURE", "description": "Send the measure frame to be emulated."},
    "5e": {"name":"CALIB_CMD_RESET", "description": "Reset meter and advance rtc, simulating a power outgage. "},
    "5f": {"name":"CALIB_CMD_RESET_BILLING_FLAG", "description": "Reset meter setting a flag in meter memory, simulating a power outgage during billing reset/demand closing."},
    "60": {"name":"CALIB_CMD_RESET_MEMORY_FLAG", "description": "Reset meter setting a flag in meter memory, simulating a power outgage memory operations."},
    "61": {"name":"CALIB_CMD_RESET_WDT_FLAG", "description": "Reset meter setting a flag for wdt simulation."},
    "62": {"name":"CALIB_CMD_TEST_RTC_CONFIG", "description": "Test RTC config."},
    "63": {"name":"CALIB_CMD_TEST_MCO_ENABLE", "description": "Extern clock to display pin."},
    "64": {"name":"CALIB_CMD_TEST_MCO_DISABLE", "description": "Extern clock to display pin."},
    "65": {"name":"CALIB_CMD_TEST_LOOP_SERIAL", "description": "Test Serial Loop Back."},
    "66": {"name":"CALIB_CMD_TEST_LOOP_IO", "description": "Test IO Loop Back."},
    "67": {"name":"CALIB_CMD_TEST_READ_FLASH_PROTECTION", "description": "Test Read Flash Protection."},
    "68": {"name":"CALIB_CMD_SPI_MEM", "description": "Block/Unblock SPI"},
    "69": {"name":"CALIB_CMD_RTC_MINUTE", "description": "generating synchronism pulses from 1 to 5 minutes."},
    "6a": {"name":"CALIB_CMD_EMUL_MEASURE_FRAME_ID9", "description": "Send the measure frame to be emulated in frame Id9."},

    "6b": {"name":"CALIB_CMD_SET_TEST_POWER_QUALITY", "description": "Test power quality configuration."},
    "6c": {"name":"CALIB_CMD_CONFIG_USER_PASSWORD", "description": "Config user password and activate."},
    "6d": {"name":"CALIB_CMD_TEST_MISCELLANEOUS_PINS", "description": "Test meter power supplies (3V3 NMS2 Enable, 9V Auxiliary Boards Enable, 3V3 Peripheral Enable e 9V Load) and External Module"},
}

abnt_commands = {
    "11": {"name":"ABNT_CMD_11", "description": "Request open a session with password"},
    "12": {"name":"ABNT_CMD_12", "description": "Change P0 password - By P0 or P5"},
    "13": {"name":"ABNT_CMD_13", "description": "Request challenge and password salt"},
    "14": {"name":"ABNT_CMD_14", "description": "Read instanteneous values"},
    "20": {"name":"ABNT_CMD_20", "description": "Read actual parameters with billing reset"},
    "21": {"name":"ABNT_CMD_21", "description": "Read actual parameters without billing reset"},
    "22": {"name":"ABNT_CMD_22", "description": "Read previous parameters with billing reset"},
    "23": {"name":"ABNT_CMD_23", "description": "Read actual registers "},
    "24": {"name":"ABNT_CMD_24", "description": "Read previous registers"},
    "25": {"name":"ABNT_CMD_25", "description": "Read power on/off periods"},
    "26": {"name":"ABNT_CMD_26", "description": "Read all load profile registers since last billing reset"},
    "27": {"name":"ABNT_CMD_27", "description": "Read all load profile registers from previous billing reset"},
    "28": {"name":"ABNT_CMD_28", "description": "leitura dos registros de altera????es"},
    "29": {"name":"ABNT_CMD_29", "description": "Program date"},
    "30": {"name":"ABNT_CMD_30", "description": "Program time"},
    "31": {"name":"ABNT_CMD_31", "description": "Program demand interval"},
    "32": {"name":"ABNT_CMD_32", "description": "Program holidays"},
    "33": {"name":"ABNT_CMD_33", "description": "Program multiplier constants"},
    "35": {"name":"ABNT_CMD_35", "description": "Program TOU"},
    "36": {"name":"ABNT_CMD_36", "description": "Program reserved tariff"},
    "37": {"name":"ABNT_CMD_37", "description": "Change the condition of meter occurrence"},
    "39": {"name":"ABNT_CMD_39", "description": "Resposta de comando nao implementado"},
    "40": {"name":"ABNT_CMD_40", "description": "Information about meter occurrences"},
    "41": {"name":"ABNT_CMD_41", "description": "Read partial registers first channel"},
    "42": {"name":"ABNT_CMD_42", "description": "Read partial registers second channel"},
    "43": {"name":"ABNT_CMD_43", "description": "Read partial registers third channel"},
    "44": {"name":"ABNT_CMD_44", "description": "Read previous partial registers first channel"},
    "45": {"name":"ABNT_CMD_45", "description": "Read previous partial registers second channel"},
    "46": {"name":"ABNT_CMD_46", "description": "Read previous partial registers third channel"},
    "51": {"name":"ABNT_CMD_51", "description": "Configure load profile readout"},
    "52": {"name":"ABNT_CMD_52", "description": "Read load profile entries"},
    "63": {"name":"ABNT_CMD_63", "description": "Program automatic demand reset"},
    "64": {"name":"ABNT_CMD_64", "description": "Program DST"},
    "65": {"name":"ABNT_CMD_65", "description": "Program TOU2"},
    "66": {"name":"ABNT_CMD_66", "description": "Program channel magnitude"},
    "67": {"name":"ABNT_CMD_67", "description": "Program reactive time table and configuration"},
    "73": {"name":"ABNT_CMD_73", "description": "Program load profile interval"},
    "76": {"name":"ABNT_CMD_76", "description": "Change division by 100 of the display quantities"},
    "77": {"name":"ABNT_CMD_77", "description": "Program tariff for saturday, sunday and holiday"},
    "78": {"name":"ABNT_CMD_78", "description": "Program tariff color"},
    "79": {"name":"ABNT_CMD_79", "description": "Change screen to shown on Display"},
    "80": {"name":"ABNT_CMD_80", "description": "Read out metrology parameters"},
    "81": {"name":"ABNT_CMD_81", "description": "Program SU type"},
    "87": {"name":"ABNT_CMD_87", "description": "Set or Read out installation code"},
    "90": {"name":"ABNT_CMD_90", "description": "Change the display view - quantity and number of digits after decimal point"},
    "92": {"name":"ABNT_CMD_92", "description": "Change the Universal Time Table"},
    "95": {"name":"ABNT_CMD_95", "description": "Change metrology parameters (kp e ke)"},
    "98": {"name":"ABNT_CMD_98", "description": "Extended command"},
    "99": {"name":"ABNT_CMD_99", "description": "Firmware download"},
    "e2": {"name":"ABNT_CMD_E2", "description": "Extended command"},
    "ff": {"name":"ABNT_CMD_EMPTY", "description": ""},
}
        
abnt_extended_commands = {
    "01": {"name":"ABNT_EXT_CMD_01", "description": "Program and read network address"},
    "04": {"name":"ABNT_EXT_CMD_04", "description": "Enable meter verification"},
    "06": {"name":"ABNT_EXT_CMD_06", "description": "Meter verification data (cmd generated by sample service)"},
    "07": {"name":"ABNT_EXT_CMD_07", "description": "Meter verification hash (cmd generated by sample service) "},
    "08": {"name":"ABNT_EXT_CMD_08", "description": "Meter verification signature (cmd generated by sample service)"},
    "0f": {"name":"ABNT_EXT_CMD_0F", "description": "Meter monitor configuration (all types)"},
    "10": {"name":"ABNT_EXT_CMD_10", "description": "Meter hash"},
    "20": {"name":"ABNT_EXT_CMD_20", "description": "Set number of digits for energy and demand to shown on display LCD"},
    "21": {"name":"ABNT_EXT_CMD_21", "description": "Read logs"},
    "22": {"name":"ABNT_EXT_CMD_22", "description": "Config time sync (GPS)"},
    "23": {"name":"ABNT_EXT_CMD_23", "description": "Read meterstatus and RTC offset"},
    "24": {"name":"ABNT_EXT_CMD_24", "description": "Config creep led"},
    "25": {"name":"ABNT_EXT_CMD_25", "description": "Read load profile"},
    "26": {"name":"ABNT_EXT_CMD_26", "description": "Write entire external data flash"},
    "27": {"name":"ABNT_EXT_CMD_27", "description": "Read entire external data flash"},
    "28": {"name":"ABNT_EXT_CMD_28", "description": "Reading production configuration (configuration sheet) "},
    "29": {"name":"ABNT_EXT_CMD_29", "description": "Reading the programmed screens"},
    "2a": {"name":"ABNT_EXT_CMD_2A", "description": "Reading info about 2 or 3 elements"},
    "2b": {"name":"ABNT_EXT_CMD_2B", "description": "Reading generic information"},
    "2c": {"name":"ABNT_EXT_CMD_2C", "description": "Reading info about display"},
    "2f": {"name":"ABNT_EXT_CMD_2F", "description": "Config network type communication"},
    "3d": {"name":"ABNT_EXT_CMD_3D", "description": "RTC TEST MODE"},
    "3f": {"name":"ABNT_EXT_CMD_3F", "description": "Data programming screen display: primary or secondary"},
    "40": {"name":"ABNT_EXT_CMD_40", "description": "Program and read prodist"},
    "41": {"name":"ABNT_EXT_CMD_41", "description": "Read DRP/DRC - prodist"},
    "42": {"name":"ABNT_EXT_CMD_42", "description": "Read monthly indicators - prodist"},
    "43": {"name":"ABNT_EXT_CMD_43", "description": "Read voltage max/min - prodist"},
    "44": {"name":"ABNT_EXT_CMD_44", "description": "Read Qos Profile - prodist"},
    "45": {"name":"ABNT_EXT_CMD_45", "description": "Read Individual Voltage Harmonics - Instantaneous"},
    "46": {"name":"ABNT_EXT_CMD_46", "description": "Read Individual Voltage Harmonics - Profile"},
    "4f": {"name":"ABNT_EXT_CMD_4F", "description": "Program password expiration time"},
    "50": {"name":"ABNT_EXT_CMD_50", "description": "Read tampers status"},
    "51": {"name":"ABNT_EXT_CMD_51", "description": "Config and  reset Tamper"},
    "53": {"name":"ABNT_EXT_CMD_53", "description": "Read power down counters"},
    "60": {"name":"ABNT_EXT_CMD_60", "description": "Controlling the Network Indicator"},
    "61": {"name":"ABNT_EXT_CMD_61", "description": "Block/Unblock writting ABNT command on optical port (only P5' has access for this command)"},
    "62": {"name":"ABNT_EXT_CMD_62", "description": "Meter warm reset - This command will reset register, logs and parameter of meter.  (Applied only ICG)"},
    "63": {"name":"ABNT_EXT_CMD_63", "description": "Speed up the metrological led"},
    "68": {"name":"ABNT_EXT_CMD_68", "description": "Meter monitor status"},
    "69": {"name":"ABNT_EXT_CMD_69", "description": "Reserved for future use, with Ethernet for multi user feature implementation"},
    "80": {"name":"ABNT_EXT_CMD_80", "description": "Program ethernet interface IPv4"},
    "81": {"name":"ABNT_EXT_CMD_81", "description": "Program ethernet interface IPv6"},
    "90": {"name":"ABNT_EXT_CMD_90", "description": "Disconnector open/close command"},
    "99": {"name":"ABNT_EXT_CMD_99", "description": "Generic calibration command encapsulation"},
    "12": {"name":"ABNT_EXT_CMD_12", "description": "Management passwords ABNT"},
    "30": {"name":"ABNT_EXT_CMD_30", "description": "microadjust RTC"},
    "32": {"name":"ABNT_EXT_CMD_32", "description": "extended holidays"},
}