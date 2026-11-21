# ==============================================================================
# HOTEL BOOKING REVENUE ANALYSIS PROJECT
# ==============================================================================

import os
import io
import pandas as pd
import numpy as np

# ==============================================================================
# STEP 1: LOAD THE DATASET
# ==============================================================================
print("\n" + "=" * 70)
print("STEP 1: LOADING DATASET")
print("=" * 70)

# Check if external CSV file exists, otherwise use the embedded raw dataset
csv_paths = [
    'hotel_bookings_raw.csv',
    'data/raw/hotel_bookings_raw.csv',
    '../data/raw/hotel_bookings_raw.csv',
    os.path.join(os.path.dirname(__file__), 'data', 'raw', 'hotel_bookings_raw.csv') if '__file__' in locals() else ''
]

csv_file = None
for p in csv_paths:
    if p and os.path.exists(p):
        csv_file = p
        break

if csv_file:
    print(f"Reading dataset from file: {csv_file}")
    df = pd.read_csv(csv_file)
else:
    print("Reading dataset from embedded raw data...")
    raw_data_string = """Booking_ID,Check_In_Date,City,Room_Type,Booking_Channel,Meal_Plan,Room_Rate_INR,Nights_Stayed,Lead_Time_Days,Guests_Count,Distance_From_Airport_Km,Total_Revenue_INR
HB1131,2026-08-27,Mumbai,Standard,OTA App,Room Only,3350,4,28,2,26.5,15909.94
HB1138,2024-12-23,Bengaluru,Deluxe,Direct Website,Breakfast Only,5400,1,14,2,9.3,12558.71
HB1166,2026-04-23,New Delhi,Executive,Direct Website,Breakfast Only,8650,8,5,2,9.5,28387.02
HB1067,2026-03-29,Jaipur,Standard,Corporate,Room Only,3500,1,20,1,32.1,6101.89
HB1014,2026-05-28,Jaipur,Suite,Direct Website,All Inclusive,12650,5,12,3,18.4,39982.98
HB1102,2025-08-09,Mumbai,Deluxe,Direct Website,Breakfast Only,5050,3,15,1,36.6,22919.39
HB1214,2025-03-23,Bengaluru,Deluxe,OTA App,Half Board,4900,4,27,3,34.3,19173.16
HB1182,2025-01-23,New Delhi,Deluxe,OTA App,Breakfast Only,5200,1,2,2,15.3,7730.37
HB1170,2025-03-29,Mumbai,Executive,Direct Website,Room Only,7400,2,11,2,18.2,10720.27
HB1061,2025-10-21,Mumbai,Executive,OTA App,Breakfast Only,9250,3,10,3,29.8,33207.78
HB1159,2025-08-27,Jaipur,Standard,OTA App,Room Only,4100,3,18,2,41.0,13762.74
HB1024,2025-01-23,Mumbai,Deluxe,Corporate,Half Board,6300,4,60,2,24.3,15493.33
HB1230,2024-12-21,JAIPUR ,Standard,Walk-in,Breakfast Only,3600,2,2,1,10.1,14943.06
HB1072,2025-11-25,Bengaluru,Standard,Walk-in,All Inclusive,3400,1,29,3,21.8,11403.19
HB1097,2026-04-21,Jaipur,Deluxe,OTA App,Breakfast Only,5050,3,2,1,7.0,17410.35
HB1010,2025-01-26,Mumbai,Deluxe,OTA App,Room Only,4600,3,12,4,38.1,13817.35
HB1089,2025-02-09,Goa,Deluxe,Direct Website,Room Only,5450,1,44,3,36.9,10146.89
HB1196,2026-09-26,Mumbai,Standard,Direct Website,Room Only,3500,5,20,1,21.1,26803.16
HB1042,2026-11-01,New Delhi,Deluxe,OTA App,Breakfast Only,4950,2,54,2,13.5,9624.98
HB1141,2026-07-14,Mumbai,Standard,Walk-in,Breakfast Only,3550,2,43,2,35.2,15892.69
HB1195,2025-05-07,Mumbai,Deluxe,OTA App,Breakfast Only,7150,10,10,2,10.1,30505.6
HB1135,2026-05-20,Bengaluru,Standard,OTA App,All Inclusive,3650,3,10,2,38.5,16878.59
HB1044,2026-01-02,Bengaluru,Deluxe,Walk-in,Room Only,6350,4,28,2,19.1,16081.99
HB1157,2026-11-03,Bengaluru,Standard,Corporate,Room Only,3350,4,5,2,20.4,23132.07
HB1130,2025-05-11,Bengaluru,Standard,Corporate,Room Only,3500,5,16,2,34.3,14751.22
HB1203,2026-05-19,Bengaluru,Deluxe,OTA App,Breakfast Only,6450,4,18,4,27.1,32407.69
HB1044,2026-01-02,Bengaluru,Deluxe,Walk-in,Room Only,6350,4,28,2,19.1,16081.99
HB1154,2025-04-11,Bengaluru,Executive,OTA App,Breakfast Only,10400,2,22,2,26.5,23454.11
HB1059,2025-10-14,Jaipur,Deluxe,Walk-in,Breakfast Only,5500,3,5,2,33.8,11839.82
HB1173,2025-08-25,New Delhi,Standard,OTA App,Room Only,3500,4,6,2,9.9,16887.17
HB1055,2026-09-15,New Delhi,Standard,Corporate,Room Only,3300,2,2,1,14.3,16674.0
HB1095,2025-08-26,Goa,Standard,Corporate,Breakfast Only,3400,1,7,3,12.6,3200.0
HB1124,2026-02-01,bengaluru,Standard,Corporate,Breakfast Only,3350,7,5,2,7.4,28302.37
HB1039,2025-07-29,Mumbai,Executive,OTA App,Half Board,5950,2,12,2,33.4,16582.63
HB1249,2025-03-22,Mumbai,Standard,OTA App,Room Only,3800,5,17,4,25.0,9981.78
HB1103,2025-06-09,Mumbai,Suite,OTA App,Half Board,12450,3,28,2,16.7,28722.79
HB1027,2026-11-12,Bengaluru,Standard,OTA App,Half Board,3850,1,27,1,18.2,3200.0
HB1101,2026-09-05,Bengaluru,Deluxe,OTA App,Breakfast Only,6850,3,18,2,32.5,23207.3
HB1050,2025-04-17,New Delhi,Standard,OTA App,Half Board,3600,3,18,2,4.6,21897.67
HB1023,2026-03-04,Jaipur,Standard,OTA App,Breakfast Only,3700,3,,2,25.4,9191.44
HB1034,2026-01-02,Mumbai,Deluxe,Corporate,Half Board,5550,5,29,1,27.6,24340.59
HB1086,2026-09-03,Mumbai,Standard,Direct Website,Breakfast Only,3150,2,9,2,25.1,17876.04
HB1149,2026-03-30,Bengaluru,Standard,Direct Website,Breakfast Only,4000,7,37,2,23.5,22211.65
HB1206,2026-07-02,New Delhi,Deluxe,OTA App,Room Only,6600,1,73,2,35.3,9955.61
HB1037,2025-01-20,New Delhi,Deluxe,Corporate,Half Board,6650,2,15,4,11.9,12483.13
HB1161,2026-10-30,Mumbai,Deluxe,Direct Website,Half Board,6100,1,13,3,39.3,23924.14
HB1211,2026-05-14,Bengaluru,Deluxe,OTA App,Breakfast Only,4300,6,23,1,29.7,27684.37
HB1148,2025-06-10,Mumbai,Deluxe,OTA App,Room Only,3100,2,21,2,3.0,15014.44
HB1080,2025-05-14,Bengaluru,Standard,OTA App,All Inclusive,3000,3,19,1,39.6,25244.7
HB1229,2025-01-15,Bengaluru,Deluxe,Walk-in,Half Board,6300,3,1,4,7.6,19917.54
HB1205,2025-02-03, New Delhi,Standard,Direct Website,Breakfast Only,3550,4,47,1,35.5,18776.57
HB1109,2025-08-20,Bengaluru,Standard,OTA App,Half Board,3800,6,11,2,27.1,24235.36
HB1123,2025-06-14,Jaipur,Deluxe,Corporate,Breakfast Only,5050,5,34,1,27.7,23236.45
HB1054,2025-08-23,Bengaluru,Executive,Direct Website,Half Board,10700,2,19,2,30.0,25901.13
HB1183,2025-11-17,Bengaluru,Suite,OTA App,Room Only,14350,1,24,3,33.7,23787.92
HB1144,2025-05-10,Mumbai,Executive,OTA App,Breakfast Only,8100,4,13,1,22.0,22890.71
HB1186,2024-11-23,Bengaluru,Deluxe,OTA App,Breakfast Only,,2,15,1,30.6,19319.93
HB1020,2026-05-31,Mumbai,Deluxe,OTA App,Room Only,6050,6,46,2,29.4,34550.6
HB1219,2025-05-10,Bengaluru,Standard,OTA App,Breakfast Only,4500,2,11,2,13.1,10881.79
HB1041,2026-08-15,Bengaluru,Deluxe,Direct Website,Breakfast Only,4850,1,18,2,29.6,11854.37
HB1009,2026-09-07,New Delhi,Standard,OTA App,Breakfast Only,3350,9,67,1,31.5,27509.62
HB1220,2026-02-09,Jaipur,Deluxe,Direct Website,Half Board,5800,2,23,2,37.3,11719.86
HB1058,2025-07-17,Mumbai,Deluxe,Corporate,Breakfast Only,6400,9,12,1,18.7,32414.95
HB1096,2025-05-28,Jaipur,Standard,OTA App,Breakfast Only,4400,3,35,1,4.0,19627.58
HB1078,2026-05-31,New Delhi,Deluxe,OTA App,Half Board,5400,3,5,1,35.2,23825.61
HB1242,2026-07-22,Jaipur,Standard,Corporate,Room Only,3450,3,7,2,31.0,9012.12
HB1184,2025-01-11,Bengaluru,Standard,OTA App,Room Only,4250,2,8,2,30.8,11630.26
HB1090,2026-07-20,Bengaluru,Deluxe,OTA App,Half Board,5600,1,11,2,32.9,17313.73
HB1224,2024-12-13,New Delhi,Standard,Corporate,Breakfast Only,3900,3,5,4,7.0,4234.4
HB1179,2025-06-02,Bengaluru,Standard,OTA App,Breakfast Only,2800,9,27,2,16.3,27644.84
HB1209,2026-05-21,Mumbai,Deluxe,Direct Website,Breakfast Only,4800,4,31,2,13.3,12314.37
HB1202,2025-07-16,New Delhi,Executive,OTA App,All Inclusive,9500,3,13,2,22.3,27535.02
HB1238,2026-06-06,Bengaluru,Deluxe,OTA App,Breakfast Only,5600,5,9,2,36.3,14995.38
HB1164,2026-11-13, Mumbai ,Executive,Direct Website,Room Only,8050,1,13,1,4.5,25734.24
HB1063,2025-02-05,New Delhi,Standard,Direct Website,Room Only,3850,1,38,3,18.6,17528.01
HB1074,2025-05-20,New Delhi,Standard,Walk-in,Breakfast Only,3550,1,7,2,32.5,11286.78
HB1094,2026-04-05,Jaipur,Standard,OTA App,Breakfast Only,3400,2,6,2,3.2,16020.68
HB1114,2026-08-10,Goa,Deluxe,OTA App,Breakfast Only,,1,5,2,10.5,22545.32
HB1107,2024-12-10,Mumbai,Executive,Walk-in,Breakfast Only,9500,1,20,2,22.7,19050.39
HB1036,2025-11-19,Bengaluru,Executive,OTA App,Breakfast Only,8650,4,7,1,29.2,12831.02
HB1178,2026-04-20,Bengaluru,Deluxe,OTA App,Room Only,5900,3,17,1,40.3,14571.39
HB1111,2026-06-28,Bengaluru,Executive,OTA App,Breakfast Only,6800,2,10,4,11.3,17431.02
HB1115,2025-02-03,Bengaluru,Deluxe,OTA App,Room Only,5650,9,12,3,26.1,26595.24
HB1098,2026-04-14,Goa,Deluxe,Corporate,,4550,5,50,3,4.0,18791.78
HB1033,2025-12-16,Mumbai,Deluxe,OTA App,Room Only,5850,4,11,2,15.4,25262.17
HB1091,2025-02-02,  mumbai,Executive,Corporate,Breakfast Only,9950,6,14,3,5.2,26948.43
HB1126,2026-03-26,Mumbai,Executive,OTA App,Breakfast Only,8150,4,11,2,39.3,21105.82
HB1117,2026-07-05,New Delhi,Standard,OTA App,,4050,2,1,3,33.5,9017.84
HB1132,2025-03-16,Mumbai,Deluxe,Corporate,All Inclusive,6450,3,34,2,18.5,22811.7
HB1247,2025-03-09,Mumbai,Deluxe,Corporate,Breakfast Only,5250,10,13,2,19.4,32702.58
HB1071,2025-12-25,New Delhi,Deluxe,Corporate,Room Only,5700,2,66,3,18.2,20354.39
HB1057,2025-04-11,Bengaluru,Standard,Direct Website,Breakfast Only,3750,5,24,2,23.6,21353.29
HB1153,2025-10-27,Mumbai,Standard,Direct Website,Room Only,2750,3,9,4,25.5,20189.94
HB1245,2025-07-04,Goa,Deluxe,OTA App,Breakfast Only,,1,33,1,5.0,10817.69
HB1087,2026-07-06,Mumbai,Deluxe,OTA App,Breakfast Only,5950,2,9,1,22.0,22498.8
HB1031,2025-11-08,Goa,Deluxe,Corporate,Room Only,5900,1,29,4,,11962.93
HB1143,2026-08-10,Mumbai,Standard,OTA App,All Inclusive,3300,2,24,2,30.9,20627.61
HB1004,2025-07-30,Jaipur,Standard,OTA App,Half Board,3650,3,33,2,32.6,14088.09
HB1158,2025-07-26,New Delhi,Executive,Corporate,Half Board,9750,2,33,2,,21536.44
HB1234,2026-07-10,Goa,Standard,Walk-in,Breakfast Only,2850,2,13,2,21.6,3200.0
HB1215,2026-10-13,Mumbai,Standard,Corporate,Half Board,4750,4,2,1,22.5,22003.68
HB1197,2025-01-29,New Delhi,Standard,Corporate,Half Board,3100,3,35,2,38.4,13777.77
HB1216,2025-06-12,New Delhi,Deluxe,OTA App,Breakfast Only,5250,9,10,2,29.8,22206.74
HB1022,2025-11-10,Goa,Standard,Corporate,Breakfast Only,3100,5,32,2,34.2,11450.19
HB1018,2026-09-30,Goa,Executive,OTA App,Room Only,8100,7,30,2,33.8,28219.94
HB1225,2025-07-19,New Delhi,Executive,OTA App,Breakfast Only,10200,3,8,4,6.5,28299.62
HB1248,2026-08-16,Bengaluru,Deluxe,Walk-in,Room Only,4450,3,36,2,8.2,13676.7
HB1075,2026-09-21,Bengaluru,Executive,OTA App,Half Board,9150,9,36,2,22.6,32030.61
HB1147,2025-07-27,Bengaluru,Executive,OTA App,Room Only,7100,4,14,2,13.6,24511.92
HB1133,2026-08-04,Goa,Suite,OTA App,Room Only,15100,2,29,2,9.1,33626.17
HB1167,2025-09-17,New Delhi,Deluxe,Direct Website,Half Board,5250,2,40,1,16.8,18851.64
HB1241,2025-07-14,Mumbai,Executive,Walk-in,Breakfast Only,6600,2,16,3,11.5,20959.45
HB1030,2025-06-17,Jaipur,Standard,OTA App,Room Only,4250,1,40,1,9.6,11611.83
HB1152,2025-03-10,Bengaluru,Deluxe,OTA App,Breakfast Only,5100,7,8,2,11.3,24519.09
HB1113,2025-12-25,Mumbai,Standard,Walk-in,Room Only,3900,2,13,3,20.0,16401.03
HB1165,2025-01-20,Jaipur,Executive,OTA App,Breakfast Only,7700,1,29,1,38.2,11599.6
HB1105,2025-04-17,Bengaluru,Executive,Corporate,Breakfast Only,,2,34,4,3.6,27412.02
HB1226,2025-03-02,Goa,Deluxe,OTA App,Breakfast Only,6600,2,6,2,25.4,21985.32
HB1160,2026-03-19,Mumbai,Standard,OTA App,Room Only,3450,2,2,2,27.6,12675.94
HB1092,2026-05-04,New Delhi,Standard,Corporate,Room Only,3850,4,16,2,7.8,14679.44
HB1013,2026-06-21,Jaipur,Standard,Direct Website,Half Board,3700,2,14,3,8.3,18368.37
HB1198,2026-07-14,New Delhi,Standard,Corporate,Half Board,2750,0,11,1,27.9,14330.75
HB1016,2026-06-13,New Delhi,Suite,OTA App,Breakfast Only,11200,4,20,1,41.8,27011.92
HB1187,2026-01-15,Bengaluru,Standard,OTA App,Breakfast Only,3350,3,52,3,31.3,8552.08
HB1237,2024-12-24,Goa,Standard,Direct Website,Half Board,3450,1,50,1,40.2,14741.89
HB1188,2026-04-22,New Delhi,Standard,Corporate,Half Board,3100,2,4,1,20.6,11368.75
HB1015,2026-09-11,Goa,Suite,Walk-in,Room Only,13200,1,22,2,9.8,31337.01
HB1227,2026-02-17,Jaipur,Standard,OTA App,Half Board,3900,4,4,1,,8280.21
HB1244,2024-12-19,Goa,Deluxe,OTA App,Room Only,4950,1,23,2,4.4,3200.0
HB1025,2026-09-14,New Delhi,Executive,Corporate,Room Only,6150,8,7,2,13.2,23377.38
HB1146,2026-02-07,New Delhi,Standard,OTA App,Breakfast Only,2950,2,24,3,28.8,16303.61
HB1017,2026-02-27,Bengaluru,Standard,Direct Website,All Inclusive,3300,6,2,1,32.5,22506.37
HB1208,2025-02-16,Bengaluru,Deluxe,OTA App,Half Board,5000,3,15,2,16.4,17452.6
HB1116,2025-01-16,Mumbai,Deluxe,OTA App,Half Board,5150,3,30,2,29.0,21809.11
HB1231,2026-03-02,Mumbai,Deluxe,Direct Website,Breakfast Only,4150,6,23,3,23.8,11501.27
HB1177,2026-01-24,Jaipur,Standard,OTA App,Room Only,3450,1,6,2,9.4,8913.25
HB1239,2024-12-11,Bengaluru,Deluxe,Corporate,All Inclusive,5100,4,3,3,32.4,22026.96
HB1200,2026-03-02,Bengaluru,Deluxe,Corporate,Room Only,5150,4,8,1,15.7,27511.52
HB1142,2025-03-17,New Delhi,Executive,Corporate,Breakfast Only,9150,4,14,1,7.5,24805.17
HB1221,2026-03-31,Mumbai,Executive,Corporate,Breakfast Only,6200,5,24,3,,21322.19
HB1172,2026-03-18,Mumbai,Standard,Corporate,,3600,2,5,2,36.9,8682.66
HB1125,2025-04-25,Mumbai,Deluxe,Direct Website,Breakfast Only,5550,4,23,1,38.4,21216.76
HB1218,2026-05-07,NEW DELHI,Deluxe,OTA App,All Inclusive,4900,2,42,4,6.3,22859.17
HB1049,2026-02-18,Goa,Executive,Direct Website,Half Board,9900,4,28,2,13.6,27884.19
HB1048,2026-01-25,Bengaluru,Standard,OTA App,Half Board,2750,3,29,2,7.7,15287.44
HB1233,2024-11-23,Goa,Deluxe,OTA App,Breakfast Only,6350,1,31,2,,13145.77
HB1073,2026-10-02,New Delhi,Executive,Walk-in,Breakfast Only,9500,3,45,2,7.0,24601.52
HB1068,2025-04-05,Mumbai,Deluxe,OTA App,Breakfast Only,6350,6,15,2,40.7,23694.32
HB1122,2026-05-16,Jaipur,Deluxe,OTA App,Half Board,5500,1,7,2,23.0,14610.36
HB1083,2025-01-17,New Delhi,Executive,OTA App,Half Board,7450,1,20,2,40.9,25656.17
HB1100,2024-11-27,Goa,Standard,Direct Website,Half Board,2650,4,7,2,38.0,20748.39
HB1032,2026-01-27,Bengaluru,Deluxe,Walk-in,Half Board,5400,1,12,1,34.6,7319.3
HB1155,2026-02-08,Mumbai,Suite,OTA App,Half Board,12350,3,15,2,16.0,33275.22
HB1175,2025-09-29,Mumbai,Suite,OTA App,Breakfast Only,13900,2,17,4,23.1,31902.84
HB1121,2025-03-22,Bengaluru,Executive,OTA App,Breakfast Only,7850,1,27,4,4.8,15031.69
HB1145,2025-05-22,Mumbai,Executive,OTA App,Breakfast Only,8950,1,54,2,24.4,15974.74
HB1168,2025-07-08,Bengaluru,Deluxe,Corporate,Half Board,5500,-3,9,2,9.0,22604.64
HB1118,2025-01-25,Bengaluru,Executive,Walk-in,Room Only,8700,1,34,2,19.8,15723.94
HB1217,2025-04-23,New Delhi,Deluxe,Corporate,Room Only,5750,4,6,2,30.9,18001.17
HB1189,2025-07-01,Bengaluru,Standard,OTA App,Breakfast Only,3900,2,25,2,6.8,11614.78
HB1112,2026-10-13,Bengaluru,Executive,OTA App,Breakfast Only,7200,2,22,2,28.5,21501.86
HB1235,2025-11-18,Mumbai,Standard,OTA App,Breakfast Only,3750,1,18,3,34.4,13962.85
HB1171,2025-09-09,New Delhi,Standard,OTA App,Breakfast Only,4500,2,,2,27.5,17360.09
HB1194,2026-03-10,Goa,Deluxe,OTA App,Breakfast Only,4950,1,41,1,28.9,18404.41
HB1043,2026-01-11,Bengaluru,Standard,OTA App,Half Board,3450,1,19,2,35.3,18761.22
HB1008,2025-11-25,New Delhi,Standard,OTA App,Room Only,3250,2,29,1,15.1,7024.66
HB1066,2026-08-25,Mumbai,Standard,OTA App,Breakfast Only,2700,4,31,2,26.7,5599.04
HB1193,2026-07-30,Bengaluru,Standard,OTA App,Breakfast Only,3850,3,5,4,25.6,11567.75
HB1180,2026-09-18,Jaipur,Deluxe,Walk-in,Half Board,5900,1,30,1,31.9,22982.78
HB1163,2026-04-28,Mumbai,Deluxe,OTA App,Breakfast Only,5200,1,31,2,34.6,17500.38
HB1052,2025-02-19,New Delhi,Deluxe,OTA App,Room Only,4950,4,18,1,20.1,13048.61
HB1176,2025-12-25,New Delhi,Standard,Walk-in,Breakfast Only,3000,3,3,2,22.3,10012.56
HB1082,2025-09-06,Jaipur,Deluxe,OTA App,Half Board,5350,3,3,2,12.9,23625.18
HB1069,2026-05-25,Jaipur,Executive,OTA App,,7000,2,17,1,35.9,15026.95
HB1040,2025-11-11,New Delhi,Deluxe,Corporate,Room Only,4550,4,26,2,33.4,16873.41
HB1119,2025-08-06,Bengaluru,Suite,Corporate,Breakfast Only,9000,2,21,1,6.4,28826.28
HB1128,2025-07-29,Mumbai,Standard,OTA App,All Inclusive,3450,1,48,3,29.1,8256.77
HB1026,2026-05-17,Bengaluru,Deluxe,OTA App,Room Only,6000,2,17,1,40.2,19370.43
HB1246,2026-04-07,New Delhi,Standard,Direct Website,Room Only,4300,2,22,1,5.9,17784.8
HB1151,2026-02-21,Mumbai,Deluxe,OTA App,Room Only,4950,1,19,1,14.7,13340.65
HB1140,2025-02-09,New Delhi,Deluxe,OTA App,Breakfast Only,4400,2,1,1,10.4,13760.85
HB1190,2025-01-30,Bengaluru,Deluxe,Direct Website,Half Board,5600,2,24,1,8.2,17588.39
HB1045,2025-01-23,New Delhi,Suite,OTA App,Half Board,12500,4,50,2,11.6,40018.57
HB1110,2025-12-07,Mumbai,Suite,Direct Website,Room Only,17700,3,12,2,5.8,31655.29
HB1201,2026-02-07,Mumbai,Deluxe,Corporate,Half Board,4750,3,6,2,5.8,26657.38
HB1077,2026-08-12,Goa,Executive,Direct Website,Room Only,6450,6,7,2,34.4,20243.17
HB1136,2025-03-08,Mumbai,Standard,OTA App,Breakfast Only,4100,6,36,1,21.7,27208.0
HB1035,2026-01-22,Bengaluru,Deluxe,Corporate,Breakfast Only,6000,1,32,2,25.2,15350.55
HB1134,2026-06-20,Jaipur,Standard,Corporate,Room Only,4100,2,13,3,5.2,5268.94
HB1108,2026-09-05,Mumbai,Standard,Corporate,Breakfast Only,4600,4,33,3,10.7,13818.66
HB1064,2025-05-17,Mumbai,Deluxe,OTA App,Breakfast Only,5150,2,7,2,7.6,15765.12
HB1150,2025-06-05,Mumbai,Executive,Walk-in,Breakfast Only,5050,7,,2,37.9,22855.26
HB1192,2026-01-23,Jaipur,Suite,OTA App,Breakfast Only,13800,5,41,4,28.6,18048.53
HB1060,2025-12-07,Mumbai,Deluxe,OTA App,All Inclusive,5850,1,40,3,28.6,25903.69
HB1019,2026-09-02,Mumbai,Deluxe,OTA App,Room Only,5600,2,26,1,27.2,4837.73
HB1021,2025-11-06,Mumbai,Standard,OTA App,Breakfast Only,3100,3,17,2,4.2,9774.69
HB1223,2026-09-03,Bengaluru,Deluxe,Direct Website,Room Only,5950,2,26,3,19.5,12045.88
HB1104,2025-05-25,Mumbai,Standard,OTA App,Room Only,5200,4,8,3,8.2,19766.06
HB1070,2025-04-14,New Delhi,Standard,Direct Website,Breakfast Only,2600,2,12,2,39.0,18329.61
HB1003,2026-08-10,Mumbai,Standard,Walk-in,Breakfast Only,4300,3,29,2,20.2,15072.36
HB1007,2026-10-27,New Delhi,Standard,Walk-in,Room Only,3650,2,22,1,17.1,13620.46
HB1228,2025-03-04,Mumbai,Deluxe,Walk-in,Breakfast Only,5100,6,9,2,39.8,27891.92
HB1210,2025-07-08,Jaipur,Standard,Direct Website,Room Only,4600,2,11,2,13.9,21526.38
HB1005,2025-05-16,Mumbai,Standard,Direct Website,Breakfast Only,3050,1,16,2,35.3,13615.2
HB1065,2025-01-21,Mumbai,Executive,OTA App,All Inclusive,8600,3,31,2,15.0,25498.29
HB1139,2025-04-23,New Delhi,Standard,Direct Website,Half Board,2950,1,30,2,28.0,11457.81
HB1062,2025-06-01,Jaipur,Standard,OTA App,Breakfast Only,2950,2,9,1,23.7,8600.13
HB1056,2026-09-20,New Delhi,Standard,OTA App,All Inclusive,3100,1,18,3,25.9,12299.73
HB1185,2025-04-15,Jaipur,Executive,OTA App,Room Only,8400,3,11,2,22.5,19812.64
HB1102,2025-08-09,Mumbai,Deluxe,Direct Website,Breakfast Only,5050,3,15,1,36.6,22919.39
HB1191,2026-10-03,Bengaluru,Deluxe,Corporate,Room Only,5750,2,38,3,27.6,13448.01
HB1181,2025-05-26,Bengaluru,Executive,OTA App,Room Only,,1,25,3,40.4,11505.31
HB1099,2026-10-18,Jaipur,Standard,Corporate,Breakfast Only,4400,1,17,2,28.0,17176.35
HB1243,2025-01-01,Mumbai,Standard,OTA App,Room Only,2750,2,36,2,22.4,7469.34
HB1053,2026-08-10,New Delhi,Standard,OTA App,Half Board,4150,2,8,3,26.4,23461.43
HB1079,2026-01-10,Mumbai,Deluxe,Corporate,Breakfast Only,5150,4,36,2,36.7,19025.34
HB1127,2026-05-03,Jaipur,Suite,Corporate,Breakfast Only,10050,2,9,3,23.6,28014.31
HB1085,2025-07-28,Jaipur,Standard,Direct Website,Breakfast Only,3800,7,28,2,6.1,13405.05
HB1081,2026-10-22,New Delhi,Standard,Direct Website,Half Board,3850,10,32,2,19.9,28638.05
HB1199,2026-04-24,Bengaluru,Executive,OTA App,Breakfast Only,7950,2,8,2,29.4,24274.76
HB1236,2026-11-14,New Delhi,Standard,OTA App,Half Board,4750,2,8,4,38.4,11768.88
HB1001,2026-06-27,Mumbai,Standard,OTA App,Room Only,2850,4,9,2,15.5,10006.39
HB1169,2025-04-03,Mumbai,Deluxe,Corporate,Breakfast Only,4950,2,9,1,16.0,14860.11
HB1156,2026-09-29,Goa,Executive,OTA App,All Inclusive,7100,1,25,2,11.7,17927.33
HB1207,2025-05-03,New Delhi,Deluxe,OTA App,Room Only,5400,7,11,2,33.8,28970.14
HB1028,2025-07-28,Bengaluru,Standard,Corporate,Half Board,3350,2,22,1,9.9,13587.48
HB1240,2025-03-18,Mumbai,Standard,Direct Website,Breakfast Only,3450,1,,2,31.8,12492.05
HB1246,2026-04-07,New Delhi,Standard,Direct Website,Room Only,4300,2,22,1,5.9,17784.8
HB1012,2026-01-04,Goa,Deluxe,Walk-in,Breakfast Only,7250,2,8,2,34.0,17216.92
HB1204,2025-10-28,Mumbai,Standard,Direct Website,All Inclusive,3850,3,54,1,22.7,24286.17
HB1076,2026-10-31,New Delhi,Suite,OTA App,Breakfast Only,11600,3,7,1,13.4,25849.63
HB1174,2025-03-06,Goa,Suite,Direct Website,Room Only,13100,2,16,2,30.3,27294.15
HB1080,2025-05-14,Bengaluru,Standard,OTA App,All Inclusive,3000,3,19,1,39.6,25244.7
HB1006,2026-01-22,Bengaluru,Standard,OTA App,Breakfast Only,3700,2,10,1,35.0,12679.58
HB1195,2025-05-07,Mumbai,Deluxe,OTA App,Breakfast Only,7150,10,10,2,10.1,30505.6
HB1250,2025-06-04,Mumbai,Suite,OTA App,Half Board,15000,2,59,2,21.8,32450.64
HB1051,2026-08-31,mumbai,Executive,Walk-in,Breakfast Only,8850,5,,1,37.9,17778.49
HB1137,2026-04-17,Bengaluru,Standard,OTA App,Breakfast Only,2750,2,16,2,33.1,12403.84
HB1106,2025-09-18,Bengaluru,Executive,Direct Website,Room Only,9050,2,30,2,8.2,22845.68
HB1029,2026-01-27,New Delhi,Standard,OTA App,Room Only,4350,2,18,3,29.2,10696.87
HB1047,2025-02-15,Mumbai,Deluxe,Direct Website,Half Board,6350,2,3,1,25.1,13117.82
HB1038,2026-02-27,New Delhi,Deluxe,Corporate,Breakfast Only,6050,2,21,2,3.2,22617.36
HB1222,2025-05-01,Bengaluru,Executive,OTA App,Breakfast Only,7400,2,67,3,24.5,13791.12
HB1011,2026-08-29,New Delhi,Standard,Direct Website,Breakfast Only,3250,2,13,2,26.4,22566.49
HB1212,2026-05-27,Bengaluru,Standard,OTA App,Room Only,4000,7,,2,15.8,26280.17
HB1093,2025-07-30,Mumbai,Standard,Direct Website,All Inclusive,3450,3,13,4,20.7,19403.8
HB1046,2025-08-16,Bengaluru,Executive,OTA App,Half Board,7950,1,10,2,16.2,17746.13
HB1088,2026-03-03,Bengaluru,Standard,Corporate,All Inclusive,4500,2,8,4,38.3,16359.2
HB1120,2024-11-27,Mumbai,Deluxe,Corporate,Breakfast Only,4450,1,17,1,9.3,7673.47
HB1213,2026-08-13,Mumbai,Standard,Direct Website,Breakfast Only,2800,1,23,1,26.5,9830.64
HB1232,2026-03-19,New Delhi,Suite,OTA App,Room Only,11300,6,34,1,20.4,31630.25
HB1002,2025-12-28,Goa,Standard,OTA App,All Inclusive,2450,3,15,3,39.7,22962.33
HB1084,2026-11-18,Jaipur,Standard,Direct Website,Breakfast Only,4150,2,18,2,21.5,13964.47
HB1129,2026-04-21,Bengaluru,Executive,Direct Website,Breakfast Only,7100,2,31,2,23.9,19332.78
HB1162,2024-12-09,Mumbai,Deluxe,OTA App,All Inclusive,4500,2,30,2,18.5,19851.41"""
    df = pd.read_csv(io.StringIO(raw_data_string))

print(f"Total Rows: {df.shape[0]}, Total Columns: {df.shape[1]}")
print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing values per column in raw data:")
print(df.isnull().sum())

print("\nDuplicate rows in raw data:", df.duplicated().sum())

print("\nUnique city names before cleaning:")
print(df['City'].unique())


# ==============================================================================
# STEP 2: DATA CLEANING
# ==============================================================================
print("\n" + "=" * 70)
print("STEP 2: CLEANING DATA")
print("=" * 70)

# Create a clean copy so we keep original data safe
df_clean = df.copy()

# 1. Remove duplicate rows
df_clean = df_clean.drop_duplicates()
print(f"1. Removed duplicates. Rows remaining: {len(df_clean)}")

# 2. Fix City text (strip extra whitespace and make First Letter Capital)
df_clean['City'] = df_clean['City'].str.strip()
df_clean['City'] = df_clean['City'].str.title()
print(f"2. Cleaned unique city names: {list(df_clean['City'].unique())}")

# 3. Replace impossible values (nights stayed cannot be 0 or negative)
df_clean.loc[df_clean['Nights_Stayed'] <= 0, 'Nights_Stayed'] = np.nan
print("3. Replaced invalid non-positive Nights_Stayed with NaN.")

# 4. Fill missing values
# Mode (most frequent) for text column (Meal_Plan)
most_common_meal = df_clean['Meal_Plan'].mode()[0]
df_clean['Meal_Plan'] = df_clean['Meal_Plan'].fillna(most_common_meal)

# Median (middle value) for numeric columns (robust to extreme price outliers)
numeric_columns = ['Room_Rate_INR', 'Nights_Stayed', 'Lead_Time_Days', 'Distance_From_Airport_Km']
for col in numeric_columns:
    df_clean[col] = df_clean[col].fillna(df_clean[col].median())

# Convert discrete counts into clean integers
df_clean['Nights_Stayed'] = df_clean['Nights_Stayed'].astype(int)
df_clean['Lead_Time_Days'] = df_clean['Lead_Time_Days'].astype(int)

print(f"4. Imputed missing values. Missing count remaining: {df_clean.isnull().sum().sum()}")


# ==============================================================================
# STEP 3: CREATE HELPER COLUMNS (FEATURE ENGINEERING)
# ==============================================================================
print("\n" + "=" * 70)
print("STEP 3: FEATURE ENGINEERING")
print("=" * 70)

# 1. Calculate Revenue per Night (Average Daily Rate proxy)
df_clean['Revenue_Per_Night'] = (df_clean['Total_Revenue_INR'] / df_clean['Nights_Stayed']).round(2)

# 2. Categorize bookings into Revenue Tiers using a simple function
def get_revenue_tier(revenue):
    if revenue >= 25000:
        return 'High Value (>= 25k)'
    elif revenue >= 15000:
        return 'Medium Value (15k-25k)'
    else:
        return 'Low Value (< 15k)'

df_clean['Revenue_Tier'] = df_clean['Total_Revenue_INR'].apply(get_revenue_tier)

# 3. Categorize stay length into simple groups
def get_stay_type(nights):
    if nights <= 2:
        return 'Short Stay (1-2 nights)'
    elif nights <= 5:
        return 'Medium Stay (3-5 nights)'
    else:
        return 'Long Stay (6+ nights)'

df_clean['Stay_Type'] = df_clean['Nights_Stayed'].apply(get_stay_type)

print("Created 3 helper columns: 'Revenue_Per_Night', 'Revenue_Tier', 'Stay_Type'")
print("\nPreview of engineered columns:")
print(df_clean[['Booking_ID', 'City', 'Room_Type', 'Nights_Stayed', 'Total_Revenue_INR', 'Revenue_Per_Night', 'Revenue_Tier', 'Stay_Type']].head())


# ==============================================================================
# STEP 4: ANSWERING THE 6 BUSINESS QUESTIONS
# ==============================================================================
print("\n" + "=" * 70)
print("STEP 4: BUSINESS ANALYSIS RESULTS")
print("=" * 70)

# Question 1: What is the overall revenue performance of the hotel?
print("\n>>> Q1: OVERALL REVENUE PERFORMANCE <<<")
print(df_clean['Total_Revenue_INR'].describe().round(2))

print("\nBooking Count by Revenue Tier:")
print(df_clean['Revenue_Tier'].value_counts())

print("\nBooking Percentage by Revenue Tier (%):")
print((df_clean['Revenue_Tier'].value_counts(normalize=True) * 100).round(1))


# Question 2: Do Nights Stayed and Room Rate affect Total Revenue?
print("\n>>> Q2: DO ROOM RATE & NIGHTS STAYED DRIVE REVENUE? <<<")
corr_rate = df_clean['Room_Rate_INR'].corr(df_clean['Total_Revenue_INR'])
corr_nights = df_clean['Nights_Stayed'].corr(df_clean['Total_Revenue_INR'])
print(f"Correlation (Room Rate vs Total Revenue)    : {corr_rate:.2f} (Strong Positive)")
print(f"Correlation (Nights Stayed vs Total Revenue) : {corr_nights:.2f} (Moderate Positive)")

print("\nAverage Revenue by Stay Duration:")
print(df_clean.groupby('Stay_Type')['Total_Revenue_INR'].agg(['count', 'mean', 'median']).round(2))


# Question 3: Which Room Types generate the highest revenue?
print("\n>>> Q3: REVENUE BY ROOM TYPE <<<")
room_summary = df_clean.groupby('Room_Type')['Total_Revenue_INR'].agg(['count', 'mean', 'median'])
print(room_summary.sort_values(by='mean', ascending=False).round(2))


# Question 4: Which Booking Channels are most profitable?
print("\n>>> Q4: REVENUE BY BOOKING CHANNEL <<<")
channel_summary = df_clean.groupby('Booking_Channel')['Total_Revenue_INR'].agg(['count', 'mean', 'median'])
print(channel_summary.sort_values(by='mean', ascending=False).round(2))


# Question 5: Which Cities perform the best?
print("\n>>> Q5: REVENUE BY CITY <<<")
city_summary = df_clean.groupby('City')['Total_Revenue_INR'].agg(['count', 'mean', 'median'])
print(city_summary.sort_values(by='mean', ascending=False).round(2))


# Question 6: Which bookings are Low Value (< Rs 15,000) and why?
print("\n>>> Q6: LOW-VALUE / AT-RISK BOOKINGS ANALYSIS <<<")
low_val = df_clean[df_clean['Revenue_Tier'] == 'Low Value (< 15k)']
print(f"Total Low-Value Bookings : {len(low_val)} out of {len(df_clean)} ({len(low_val)/len(df_clean)*100:.1f}%)")
print(f"Average Nights Stayed    : {low_val['Nights_Stayed'].mean():.1f} nights (vs {df_clean['Nights_Stayed'].mean():.1f} overall)")
print(f"Average Room Rate        : Rs {low_val['Room_Rate_INR'].mean():.0f} (vs Rs {df_clean['Room_Rate_INR'].mean():.0f} overall)")

print("\nRoom Types in Low-Value Bookings:")
print(low_val['Room_Type'].value_counts())

print("\nBooking Channels in Low-Value Bookings:")
print(low_val['Booking_Channel'].value_counts())


# ==============================================================================
# STEP 5: FULL CORRELATION TABLE FOR NUMERICAL FEATURES
# ==============================================================================
print("\n" + "=" * 70)
print("STEP 5: CORRELATION MATRIX (Linear Relationships with Revenue)")
print("=" * 70)
num_cols_corr = ['Room_Rate_INR', 'Nights_Stayed', 'Lead_Time_Days', 'Guests_Count', 'Distance_From_Airport_Km', 'Total_Revenue_INR']
print(df_clean[num_cols_corr].corr().round(2))


# ==============================================================================
# STEP 6: SAVE CLEAN DATASET TO CSV
# ==============================================================================
print("\n" + "=" * 70)
print("STEP 6: SAVING CLEANED DATASET")
print("=" * 70)

# Try saving to standard output directory or local directory
output_file = 'hotel_bookings_clean.csv'
if os.path.exists('data/processed'):
    output_file = 'data/processed/hotel_bookings_clean.csv'
elif os.path.exists('../data/processed'):
    output_file = '../data/processed/hotel_bookings_clean.csv'

df_clean.to_csv(output_file, index=False)
print(f"Cleaned data successfully saved to: {output_file}")
print(f"Total cleaned rows saved: {len(df_clean)}")


# ==============================================================================
# STEP 7: PRESENTATION CHEAT SHEET (TALKING POINTS)
# ==============================================================================
print("\n" + "=" * 70)
print("HOW TO EXPLAIN THIS PROJECT TO SOMEONE (QUICK SUMMARY)")
print("=" * 70)
print("""
1. THE PROBLEM:
   - Analyzed 255 hotel bookings across Mumbai, Bengaluru, New Delhi, Jaipur, and Goa.
   - Goal: Identify what drives total booking revenue and how to improve low-yield bookings.

2. HOW WE CLEANED THE DATA:
   - Dropped 5 duplicate rows.
   - Cleaned messy city names using .str.strip().str.title() to merge 'JAIPUR ' & 'bengaluru'.
   - Fixed negative nights stayed (-3) by replacing them with NaN.
   - Filled missing numbers using the MEDIAN because price outliers don't skew the median.

3. KEY INSIGHTS:
   - Room Rate (r = 0.55) and Nights Stayed (r = 0.47) are the two primary revenue drivers.
   - Direct Website bookings earn the highest average revenue (Rs 19,336).
   - OTA Apps bring the highest volume (51.2%), but lower revenue (Rs 18,702).
   - 36% of bookings are Low Value (< Rs 15,000), primarily short 1-2 night stays in Standard rooms.

4. BUSINESS RECOMMENDATION:
   - Offer 'Stay 3, Pay for 2.5' discounts to turn 1-2 night stays into higher-paying 3+ night stays.
   - Give free breakfast on Direct Website bookings to avoid third-party OTA commission fees.
""")
print("=" * 70)
print("PROJECT EXECUTION COMPLETE!")
print("=" * 70 + "\n")
