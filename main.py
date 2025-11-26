import requests
from dataclasses import dataclass, asdict
import time


KIOSK_ID = "demo1"
BASE_URL = "https://novel.rosq.co.kr:8488"
AUTH_GET_TOKEN_PATH = "/api/auth-kiosk"
AUTH_USER_PATH = "/api/auth-user"
SET_RESULT_PATH = "/api/set-result"

USER_PHONE_1 = "01092996635" # 임재영
USER_PHONE_2 = "01052692446" # 서정환
USER_PHONE_3 = "01071402537" # 이은석
USER_PHONE_4 = "01083450332" # 이근우 
USER_PHONE_5 = "01072226635" # Lim Jae Young

BP = "BP"
HS = "HS"
BC = "BC"
ST="ST"
LU = "LU"
BS ="BS"
AL="AL"
BC="BC"
CM="CM"
VA="VA"

HEADERS = {"Content-Type": "application/json"}


BP_DUMY = [
    {"high": 118, "low": 76, "pulse": 68, "status": "정상"},
    {"high": 125, "low": 81, "pulse": 72, "status": "주의혈압"},
    {"high": 132, "low": 84, "pulse": 75, "status": "전고혈압"},
    {"high": 145, "low": 92, "pulse": 80, "status": "고혈압1기"},
    {"high": 162, "low": 102, "pulse": 85, "status": "고혈압2기"},
    {"high": 115, "low": 74, "pulse": 66, "status": "정상"},
    {"high": 128, "low": 82, "pulse": 70, "status": "주의혈압"},
    {"high": 134, "low": 86, "pulse": 77, "status": "전고혈압"},
    {"high": 148, "low": 95, "pulse": 82, "status": "고혈압1기"},
    {"high": 170, "low": 108, "pulse": 90, "status": "고혈압2기"},
    {"high": 116, "low": 75, "pulse": 65, "status": "정상"},
    {"high": 126, "low": 80, "pulse": 69, "status": "주의혈압"},
    {"high": 138, "low": 88, "pulse": 78, "status": "전고혈압"},
    {"high": 150, "low": 97, "pulse": 83, "status": "고혈압1기"},
    {"high": 165, "low": 105, "pulse": 88, "status": "고혈압2기"},
    {"high": 119, "low": 73, "pulse": 67, "status": "정상"},
    {"high": 129, "low": 83, "pulse": 71, "status": "주의혈압"},
    {"high": 136, "low": 87, "pulse": 76, "status": "전고혈압"},
    {"high": 146, "low": 94, "pulse": 79, "status": "고혈압1기"},
    {"high": 172, "low": 110, "pulse": 92, "status": "고혈압2기"},
]

HS_DUMY = [
  { "height": 170, "weight": 52, "bmi": 18.0, "status": "저체중",    "datatime": "2024-07-10 13:00:00" },
  { "height": 170, "weight": 58, "bmi": 21.3, "status": "정상",      "datatime": "2024-07-11 13:00:00" },
  { "height": 170, "weight": 73, "bmi": 24.7, "status": "비만전단계", "datatime": "2024-07-12 13:00:00" },
  { "height": 170, "weight": 78, "bmi": 27.6, "status": "1단계비만", "datatime": "2024-07-13 13:00:00" },
  { "height": 170, "weight": 92, "bmi": 31.8, "status": "2단계비만", "datatime": "2024-07-14 13:00:00" },

  { "height": 170, "weight": 43, "bmi": 16.8, "status": "저체중",    "datatime": "2024-07-15 13:00:00" },
  { "height": 170, "weight": 52, "bmi": 20.8, "status": "정상",      "datatime": "2024-07-16 13:00:00" },
  { "height": 170, "weight": 77, "bmi": 25.1, "status": "비만전단계", "datatime": "2024-07-17 13:00:00" },
  { "height": 170, "weight": 80, "bmi": 28.0, "status": "1단계비만", "datatime": "2024-07-18 13:00:00" },
  { "height": 170, "weight": 92, "bmi": 33.4, "status": "2단계비만", "datatime": "2024-07-19 13:00:00" },

  { "height": 170, "weight": 54, "bmi": 18.0, "status": "저체중",    "datatime": "2024-07-20 13:00:00" },
  { "height": 170, "weight": 72, "bmi": 22.2, "status": "정상",      "datatime": "2024-07-21 13:00:00" },
  { "height": 170, "weight": 66, "bmi": 25.2, "status": "비만전단계", "datatime": "2024-07-22 13:00:00" },
  { "height": 170, "weight": 78, "bmi": 28.0, "status": "1단계비만", "datatime": "2024-07-23 13:00:00" },
  { "height": 171, "weight": 97, "bmi": 33.2, "status": "2단계비만", "datatime": "2024-07-24 13:00:00" },

  { "height": 170, "weight": 38, "bmi": 15.8, "status": "저체중",    "datatime": "2024-07-25 13:00:00" },
  { "height": 170, "weight": 59, "bmi": 21.9, "status": "정상",      "datatime": "2024-07-26 13:00:00" },
  { "height": 170, "weight": 80, "bmi": 25.2, "status": "비만전단계", "datatime": "2024-07-27 13:00:00" },
  { "height": 170, "weight": 85, "bmi": 29.8, "status": "1단계비만", "datatime": "2024-07-28 13:00:00" }
]


BC_DUMY = [
  {
    "weight": "62.4",
    "weight_result": "표준",
    "fatyang": "14.2",
    "fatyang_result": "표준",
    "muscleyang": "25.8",
    "muscleyang_result": "표준",
    "adult_bodytype": "표준",
    "basalmetabolism": "1480",
    "golgyeokgeunyang": "29.0",
    "bmi": "21.6",
    "fatryul": "22.1",
    "fatryul_result": "표준",
    "naejangfat_level": "6",
    "wateryang": "39.8",
    "mineralsyang": "3.4",
    "proteinyang": "8.0",
    "total_grade": "82",
    "datatime": "2024-07-10 13:00:00"
  },
  {
    "weight": "68.2",
    "weight_result": "표준이상",
    "fatyang": "16.4",
    "fatyang_result": "표준이상",
    "muscleyang": "27.5",
    "muscleyang_result": "표준",
    "adult_bodytype": "비만전단계",
    "basalmetabolism": "1550",
    "golgyeokgeunyang": "30.2",
    "bmi": "23.5",
    "fatryul": "24.0",
    "fatryul_result": "표준이상",
    "naejangfat_level": "7",
    "wateryang": "40.5",
    "mineralsyang": "3.6",
    "proteinyang": "8.4",
    "total_grade": "78",
    "datatime": "2024-07-11 13:00:00"
  },
  {
    "weight": "75.6",
    "weight_result": "표준이상",
    "fatyang": "20.3",
    "fatyang_result": "표준이상",
    "muscleyang": "29.1",
    "muscleyang_result": "표준",
    "adult_bodytype": "비만",
    "basalmetabolism": "1605",
    "golgyeokgeunyang": "31.8",
    "bmi": "25.4",
    "fatryul": "26.9",
    "fatryul_result": "표준이상",
    "naejangfat_level": "9",
    "wateryang": "41.2",
    "mineralsyang": "3.8",
    "proteinyang": "8.8",
    "total_grade": "71",
    "datatime": "2024-07-12 13:00:00"
  },
  {
    "weight": "58.1",
    "weight_result": "표준",
    "fatyang": "12.1",
    "fatyang_result": "표준",
    "muscleyang": "24.7",
    "muscleyang_result": "표준",
    "adult_bodytype": "표준",
    "basalmetabolism": "1400",
    "golgyeokgeunyang": "28.0",
    "bmi": "20.2",
    "fatryul": "20.1",
    "fatryul_result": "표준",
    "naejangfat_level": "5",
    "wateryang": "38.4",
    "mineralsyang": "3.3",
    "proteinyang": "7.8",
    "total_grade": "88",
    "datatime": "2024-07-13 13:00:00"
  },
  {
    "weight": "82.3",
    "weight_result": "표준이상",
    "fatyang": "25.8",
    "fatyang_result": "표준이상",
    "muscleyang": "30.5",
    "muscleyang_result": "표준",
    "adult_bodytype": "비만",
    "basalmetabolism": "1700",
    "golgyeokgeunyang": "33.1",
    "bmi": "28.3",
    "fatryul": "29.4",
    "fatryul_result": "표준이상",
    "naejangfat_level": "12",
    "wateryang": "42.0",
    "mineralsyang": "3.9",
    "proteinyang": "9.1",
    "total_grade": "64",
    "datatime": "2024-07-14 13:00:00"
  },
  {
    "weight": "60.0",
    "weight_result": "표준",
    "fatyang": "13.5",
    "fatyang_result": "표준",
    "muscleyang": "25.2",
    "muscleyang_result": "표준",
    "adult_bodytype": "표준",
    "basalmetabolism": "1440",
    "golgyeokgeunyang": "28.5",
    "bmi": "20.9",
    "fatryul": "21.5",
    "fatryul_result": "표준",
    "naejangfat_level": "6",
    "wateryang": "39.0",
    "mineralsyang": "3.4",
    "proteinyang": "8.0",
    "total_grade": "85",
    "datatime": "2024-07-15 13:00:00"
  },
  {
    "weight": "70.2",
    "weight_result": "표준이상",
    "fatyang": "17.8",
    "fatyang_result": "표준이상",
    "muscleyang": "28.4",
    "muscleyang_result": "표준",
    "adult_bodytype": "비만전단계",
    "basalmetabolism": "1555",
    "golgyeokgeunyang": "30.6",
    "bmi": "23.8",
    "fatryul": "24.9",
    "fatryul_result": "표준이상",
    "naejangfat_level": "8",
    "wateryang": "40.7",
    "mineralsyang": "3.7",
    "proteinyang": "8.6",
    "total_grade": "77",
    "datatime": "2024-07-16 13:00:00"
  },
  {
    "weight": "77.1",
    "weight_result": "표준이상",
    "fatyang": "21.2",
    "fatyang_result": "표준이상",
    "muscleyang": "29.0",
    "muscleyang_result": "표준",
    "adult_bodytype": "비만",
    "basalmetabolism": "1610",
    "golgyeokgeunyang": "31.3",
    "bmi": "25.8",
    "fatryul": "27.3",
    "fatryul_result": "표준이상",
    "naejangfat_level": "10",
    "wateryang": "41.5",
    "mineralsyang": "3.8",
    "proteinyang": "8.9",
    "total_grade": "70",
    "datatime": "2024-07-17 13:00:00"
  },
  {
    "weight": "55.6",
    "weight_result": "표준",
    "fatyang": "11.0",
    "fatyang_result": "표준",
    "muscleyang": "24.1",
    "muscleyang_result": "표준",
    "adult_bodytype": "표준",
    "basalmetabolism": "1380",
    "golgyeokgeunyang": "27.0",
    "bmi": "19.7",
    "fatryul": "19.8",
    "fatryul_result": "표준",
    "naejangfat_level": "5",
    "wateryang": "38.0",
    "mineralsyang": "3.2",
    "proteinyang": "7.5",
    "total_grade": "90",
    "datatime": "2024-07-18 13:00:00"
  },
  {
    "weight": "83.4",
    "weight_result": "표준이상",
    "fatyang": "26.4",
    "fatyang_result": "표준이상",
    "muscleyang": "30.2",
    "muscleyang_result": "표준",
    "adult_bodytype": "비만",
    "basalmetabolism": "1710",
    "golgyeokgeunyang": "33.5",
    "bmi": "28.6",
    "fatryul": "30.1",
    "fatryul_result": "표준이상",
    "naejangfat_level": "12",
    "wateryang": "42.3",
    "mineralsyang": "4.0",
    "proteinyang": "9.3",
    "total_grade": "62",
    "datatime": "2024-07-19 13:00:00"
  },
  {
    "weight": "61.5",
    "weight_result": "표준",
    "fatyang": "13.1",
    "fatyang_result": "표준",
    "muscleyang": "25.0",
    "muscleyang_result": "표준",
    "adult_bodytype": "표준",
    "basalmetabolism": "1450",
    "golgyeokgeunyang": "28.3",
    "bmi": "21.3",
    "fatryul": "21.8",
    "fatryul_result": "표준",
    "naejangfat_level": "6",
    "wateryang": "39.3",
    "mineralsyang": "3.4",
    "proteinyang": "8.0",
    "total_grade": "80",
    "datatime": "2024-07-20 13:00:00"
  },
  {
    "weight": "72.0",
    "weight_result": "표준이상",
    "fatyang": "18.2",
    "fatyang_result": "표준이상",
    "muscleyang": "28.8",
    "muscleyang_result": "표준",
    "adult_bodytype": "비만전단계",
    "basalmetabolism": "1560",
    "golgyeokgeunyang": "31.0",
    "bmi": "24.1",
    "fatryul": "25.1",
    "fatryul_result": "표준이상",
    "naejangfat_level": "8",
    "wateryang": "40.9",
    "mineralsyang": "3.7",
    "proteinyang": "8.6",
    "total_grade": "76",
    "datatime": "2024-07-21 13:00:00"
  },
  {
    "weight": "78.9",
    "weight_result": "표준이상",
    "fatyang": "22.0",
    "fatyang_result": "표준이상",
    "muscleyang": "29.5",
    "muscleyang_result": "표준",
    "adult_bodytype": "비만",
    "basalmetabolism": "1625",
    "golgyeokgeunyang": "32.0",
    "bmi": "26.2",
    "fatryul": "28.0",
    "fatryul_result": "표준이상",
    "naejangfat_level": "10",
    "wateryang": "41.7",
    "mineralsyang": "3.8",
    "proteinyang": "9.0",
    "total_grade": "69",
    "datatime": "2024-07-22 13:00:00"
  },
  {
    "weight": "56.4",
    "weight_result": "표준",
    "fatyang": "11.5",
    "fatyang_result": "표준",
    "muscleyang": "24.3",
    "muscleyang_result": "표준",
    "adult_bodytype": "표준",
    "basalmetabolism": "1385",
    "golgyeokgeunyang": "27.4",
    "bmi": "19.9",
    "fatryul": "20.4",
    "fatryul_result": "표준",
    "naejangfat_level": "5",
    "wateryang": "38.2",
    "mineralsyang": "3.2",
    "proteinyang": "7.6",
    "total_grade": "92",
    "datatime": "2024-07-23 13:00:00"
  },
  {
    "weight": "85.0",
    "weight_result": "표준이상",
    "fatyang": "27.1",
    "fatyang_result": "표준이상",
    "muscleyang": "30.8",
    "muscleyang_result": "표준",
    "adult_bodytype": "비만",
    "basalmetabolism": "1730",
    "golgyeokgeunyang": "34.1",
    "bmi": "29.1",
    "fatryul": "30.5",
    "fatryul_result": "표준이상",
    "naejangfat_level": "12",
    "wateryang": "42.5",
    "mineralsyang": "4.0",
    "proteinyang": "9.4",
    "total_grade": "60",
    "datatime": "2024-07-24 13:00:00"
  },
  {
    "weight": "64.3",
    "weight_result": "표준",
    "fatyang": "15.0",
    "fatyang_result": "표준",
    "muscleyang": "26.4",
    "muscleyang_result": "표준",
    "adult_bodytype": "표준",
    "basalmetabolism": "1495",
    "golgyeokgeunyang": "29.5",
    "bmi": "22.0",
    "fatryul": "22.8",
    "fatryul_result": "표준",
    "naejangfat_level": "6",
    "wateryang": "40.1",
    "mineralsyang": "3.5",
    "proteinyang": "8.1",
    "total_grade": "81",
    "datatime": "2024-07-25 13:00:00"
  },
  {
    "weight": "74.8",
    "weight_result": "표준이상",
    "fatyang": "19.0",
    "fatyang_result": "표준이상",
    "muscleyang": "28.9",
    "muscleyang_result": "표준",
    "adult_bodytype": "비만전단계",
    "basalmetabolism": "1580",
    "golgyeokgeunyang": "31.2",
    "bmi": "24.9",
    "fatryul": "25.6",
    "fatryul_result": "표준이상",
    "naejangfat_level": "9",
    "wateryang": "41.0",
    "mineralsyang": "3.7",
    "proteinyang": "8.7",
    "total_grade": "75",
    "datatime": "2024-07-26 13:00:00"
  },
  {
    "weight": "74.8",
    "weight_result": "표준이상",
    "fatyang": "19.0",
    "fatyang_result": "표준이상",
    "muscleyang": "28.9",
    "muscleyang_result": "표준",
    "adult_bodytype": "비만전단계",
    "basalmetabolism": "1580",
    "golgyeokgeunyang": "31.2",
    "bmi": "24.9",
    "fatryul": "25.6",
    "fatryul_result": "표준이상",
    "naejangfat_level": "9",
    "wateryang": "41.0",
    "mineralsyang": "3.7",
    "proteinyang": "8.7",
    "total_grade": "75",
    "datatime": "2024-07-26 13:00:00"
  }
]


ST_DUMY= [
  {
    "heartrate_avg": "68",
    "heartrate_score": "85.2",
    "heartrate_step": "좋음",
    "heartrate_ng": "0",
    "jayul_activity_score": "90.4",
    "jayul_activity_step": "매우좋음",
    "piro_score": "92.1",
    "piro_step": "매우좋음",
    "heart_stability_score": "82.5",
    "heart_stability_step": "좋음",
    "jayul_balance_step": "88.0",
    "physical_stress_score": "78.2",
    "physical_stress_step": "좋음",
    "mental_stress_score": "81.5",
    "mental_stress_step": "좋음",
    "stress_ability_score": "87.1",
    "stress_ability_step": "매우좋음",
    "total_grade": "91.2",
    "dongmaek_tansung_score": "84.7",
    "dongmaek_tansung_step": "좋음",
    "malcho_tansung_score": "88.5",
    "malcho_tansung_step": "매우좋음",
    "bloodvessel_age": "25",
    "bloodvessel_score": "95.0",
    "bloodvessel_step": "1",
    "bloodvessel_step_status": "매우좋음",
    "datatime": "2024-07-10 13:00:00"
  },
  {
    "heartrate_avg": "72",
    "heartrate_score": "82.1",
    "heartrate_step": "좋음",
    "heartrate_ng": "1",
    "jayul_activity_score": "88.0",
    "jayul_activity_step": "좋음",
    "piro_score": "85.5",
    "piro_step": "좋음",
    "heart_stability_score": "79.5",
    "heart_stability_step": "좋음",
    "jayul_balance_step": "82.3",
    "physical_stress_score": "75.0",
    "physical_stress_step": "좋음",
    "mental_stress_score": "78.4",
    "mental_stress_step": "좋음",
    "stress_ability_score": "80.2",
    "stress_ability_step": "좋음",
    "total_grade": "88.4",
    "dongmaek_tansung_score": "80.1",
    "dongmaek_tansung_step": "좋음",
    "malcho_tansung_score": "82.9",
    "malcho_tansung_step": "좋음",
    "bloodvessel_age": "28",
    "bloodvessel_score": "90.3",
    "bloodvessel_step": "1",
    "bloodvessel_step_status": "좋음",
    "datatime": "2024-07-11 13:00:00"
  },
  {
    "heartrate_avg": "65",
    "heartrate_score": "88.0",
    "heartrate_step": "좋음",
    "heartrate_ng": "0",
    "jayul_activity_score": "91.2",
    "jayul_activity_step": "매우좋음",
    "piro_score": "89.9",
    "piro_step": "좋음",
    "heart_stability_score": "86.5",
    "heart_stability_step": "매우좋음",
    "jayul_balance_step": "90.4",
    "physical_stress_score": "82.0",
    "physical_stress_step": "좋음",
    "mental_stress_score": "84.3",
    "mental_stress_step": "좋음",
    "stress_ability_score": "89.0",
    "stress_ability_step": "매우좋음",
    "total_grade": "92.0",
    "dongmaek_tansung_score": "87.2",
    "dongmaek_tansung_step": "매우좋음",
    "malcho_tansung_score": "90.1",
    "malcho_tansung_step": "매우좋음",
    "bloodvessel_age": "23",
    "bloodvessel_score": "96.7",
    "bloodvessel_step": "1",
    "bloodvessel_step_status": "매우좋음",
    "datatime": "2024-07-12 13:00:00"
  },

  {
    "heartrate_avg": "74",
    "heartrate_score": "70.5",
    "heartrate_step": "보통",
    "heartrate_ng": "2",
    "jayul_activity_score": "72.0",
    "jayul_activity_step": "보통",
    "piro_score": "74.4",
    "piro_step": "보통",
    "heart_stability_score": "66.1",
    "heart_stability_step": "보통",
    "jayul_balance_step": "70.5",
    "physical_stress_score": "64.0",
    "physical_stress_step": "보통",
    "mental_stress_score": "67.5",
    "mental_stress_step": "보통",
    "stress_ability_score": "72.3",
    "stress_ability_step": "보통",
    "total_grade": "72.0",
    "dongmaek_tansung_score": "68.9",
    "dongmaek_tansung_step": "보통",
    "malcho_tansung_score": "71.0",
    "malcho_tansung_step": "보통",
    "bloodvessel_age": "35",
    "bloodvessel_score": "80.3",
    "bloodvessel_step": "2",
    "bloodvessel_step_status": "보통",
    "datatime": "2024-07-13 13:00:00"
  },
  {
    "heartrate_avg": "78",
    "heartrate_score": "68.4",
    "heartrate_step": "보통",
    "heartrate_ng": "1",
    "jayul_activity_score": "70.1",
    "jayul_activity_step": "보통",
    "piro_score": "69.8",
    "piro_step": "보통",
    "heart_stability_score": "62.3",
    "heart_stability_step": "보통",
    "jayul_balance_step": "67.3",
    "physical_stress_score": "61.2",
    "physical_stress_step": "보통",
    "mental_stress_score": "65.0",
    "mental_stress_step": "보통",
    "stress_ability_score": "68.1",
    "stress_ability_step": "보통",
    "total_grade": "68.0",
    "dongmaek_tansung_score": "63.9",
    "dongmaek_tansung_step": "보통",
    "malcho_tansung_score": "66.3",
    "malcho_tansung_step": "보통",
    "bloodvessel_age": "38",
    "bloodvessel_score": "78.0",
    "bloodvessel_step": "2",
    "bloodvessel_step_status": "보통",
    "datatime": "2024-07-14 13:00:00"
  },
  {
    "heartrate_avg": "76",
    "heartrate_score": "72.5",
    "heartrate_step": "보통",
    "heartrate_ng": "0",
    "jayul_activity_score": "71.3",
    "jayul_activity_step": "보통",
    "piro_score": "70.0",
    "piro_step": "보통",
    "heart_stability_score": "65.5",
    "heart_stability_step": "보통",
    "jayul_balance_step": "69.1",
    "physical_stress_score": "63.4",
    "physical_stress_step": "보통",
    "mental_stress_score": "66.2",
    "mental_stress_step": "보통",
    "stress_ability_score": "70.5",
    "stress_ability_step": "보통",
    "total_grade": "71.2",
    "dongmaek_tansung_score": "67.0",
    "dongmaek_tansung_step": "보통",
    "malcho_tansung_score": "69.3",
    "malcho_tansung_step": "보통",
    "bloodvessel_age": "36",
    "bloodvessel_score": "79.3",
    "bloodvessel_step": "2",
    "bloodvessel_step_status": "보통",
    "datatime": "2024-07-15 13:00:00"
  },

  {
    "heartrate_avg": "82",
    "heartrate_score": "48.0",
    "heartrate_step": "나쁨",
    "heartrate_ng": "3",
    "jayul_activity_score": "52.2",
    "jayul_activity_step": "나쁨",
    "piro_score": "55.0",
    "piro_step": "보통",
    "heart_stability_score": "49.5",
    "heart_stability_step": "나쁨",
    "jayul_balance_step": "55.3",
    "physical_stress_score": "58.4",
    "physical_stress_step": "보통",
    "mental_stress_score": "50.2",
    "mental_stress_step": "나쁨",
    "stress_ability_score": "52.1",
    "stress_ability_step": "나쁨",
    "total_grade": "54.2",
    "dongmaek_tansung_score": "50.3",
    "dongmaek_tansung_step": "나쁨",
    "malcho_tansung_score": "53.0",
    "malcho_tansung_step": "나쁨",
    "bloodvessel_age": "55",
    "bloodvessel_score": "60.1",
    "bloodvessel_step": "3",
    "bloodvessel_step_status": "나쁨",
    "datatime": "2024-07-16 13:00:00"
  },
  {
    "heartrate_avg": "85",
    "heartrate_score": "45.1",
    "heartrate_step": "나쁨",
    "heartrate_ng": "4",
    "jayul_activity_score": "50.0",
    "jayul_activity_step": "나쁨",
    "piro_score": "52.4",
    "piro_step": "나쁨",
    "heart_stability_score": "48.1",
    "heart_stability_step": "나쁨",
    "jayul_balance_step": "53.2",
    "physical_stress_score": "55.1",
    "physical_stress_step": "보통",
    "mental_stress_score": "48.0",
    "mental_stress_step": "나쁨",
    "stress_ability_score": "50.3",
    "stress_ability_step": "나쁨",
    "total_grade": "51.4",
    "dongmaek_tansung_score": "48.0",
    "dongmaek_tansung_step": "나쁨",
    "malcho_tansung_score": "51.5",
    "malcho_tansung_step": "나쁨",
    "bloodvessel_age": "60",
    "bloodvessel_score": "58.0",
    "bloodvessel_step": "3",
    "bloodvessel_step_status": "나쁨",
    "datatime": "2024-07-17 13:00:00"
  },
  {
    "heartrate_avg": "88",
    "heartrate_score": "40.3",
    "heartrate_step": "나쁨",
    "heartrate_ng": "5",
    "jayul_activity_score": "48.2",
    "jayul_activity_step": "나쁨",
    "piro_score": "50.1",
    "piro_step": "나쁨",
    "heart_stability_score": "46.0",
    "heart_stability_step": "나쁨",
    "jayul_balance_step": "51.5",
    "physical_stress_score": "53.0",
    "physical_stress_step": "보통",
    "mental_stress_score": "45.4",
    "mental_stress_step": "나쁨",
    "stress_ability_score": "48.5",
    "stress_ability_step": "나쁨",
    "total_grade": "48.2",
    "dongmaek_tansung_score": "45.4",
    "dongmaek_tansung_step": "나쁨",
    "malcho_tansung_score": "49.0",
    "malcho_tansung_step": "나쁨",
    "bloodvessel_age": "63",
    "bloodvessel_score": "55.3",
    "bloodvessel_step": "3",
    "bloodvessel_step_status": "나쁨",
    "datatime": "2024-07-18 13:00:00"
  },

  {
    "heartrate_avg": "77",
    "heartrate_score": "60.0",
    "heartrate_step": "보통",
    "heartrate_ng": "1",
    "jayul_activity_score": "62.1",
    "jayul_activity_step": "보통",
    "piro_score": "61.2",
    "piro_step": "보통",
    "heart_stability_score": "58.9",
    "heart_stability_step": "보통",
    "jayul_balance_step": "60.4",
    "physical_stress_score": "59.0",
    "physical_stress_step": "보통",
    "mental_stress_score": "60.4",
    "mental_stress_step": "보통",
    "stress_ability_score": "63.2",
    "stress_ability_step": "보통",
    "total_grade": "63.0",
    "dongmaek_tansung_score": "59.4",
    "dongmaek_tansung_step": "보통",
    "malcho_tansung_score": "61.0",
    "malcho_tansung_step": "보통",
    "bloodvessel_age": "42",
    "bloodvessel_score": "70.5",
    "bloodvessel_step": "2",
    "bloodvessel_step_status": "보통",
    "datatime": "2024-07-19 13:00:00"
  },
  {
    "heartrate_avg": "79",
    "heartrate_score": "62.4",
    "heartrate_step": "보통",
    "heartrate_ng": "1",
    "jayul_activity_score": "64.0",
    "jayul_activity_step": "보통",
    "piro_score": "63.5",
    "piro_step": "보통",
    "heart_stability_score": "59.8",
    "heart_stability_step": "보통",
    "jayul_balance_step": "61.2",
    "physical_stress_score": "60.2",
    "physical_stress_step": "보통",
    "mental_stress_score": "61.0",
    "mental_stress_step": "보통",
    "stress_ability_score": "65.2",
    "stress_ability_step": "보통",
    "total_grade": "64.5",
    "dongmaek_tansung_score": "60.5",
    "dongmaek_tansung_step": "보통",
    "malcho_tansung_score": "62.3",
    "malcho_tansung_step": "보통",
    "bloodvessel_age": "39",
    "bloodvessel_score": "72.0",
    "bloodvessel_step": "2",
    "bloodvessel_step_status": "보통",
    "datatime": "2024-07-20 13:00:00"
  },
  {
    "heartrate_avg": "81",
    "heartrate_score": "65.1",
    "heartrate_step": "보통",
    "heartrate_ng": "2",
    "jayul_activity_score": "66.0",
    "jayul_activity_step": "보통",
    "piro_score": "64.1",
    "piro_step": "보통",
    "heart_stability_score": "61.1",
    "heart_stability_step": "보통",
    "jayul_balance_step": "63.2",
    "physical_stress_score": "61.5",
    "physical_stress_step": "보통",
    "mental_stress_score": "63.3",
    "mental_stress_step": "보통",
    "stress_ability_score": "66.8",
    "stress_ability_step": "보통",
    "total_grade": "66.0",
    "dongmaek_tansung_score": "62.1",
    "dongmaek_tansung_step": "보통",
    "malcho_tansung_score": "64.0",
    "malcho_tansung_step": "보통",
    "bloodvessel_age": "41",
    "bloodvessel_score": "73.8",
    "bloodvessel_step": "2",
    "bloodvessel_step_status": "보통",
    "datatime": "2024-07-21 13:00:00"
  },

  {
    "heartrate_avg": "83",
    "heartrate_score": "52.1",
    "heartrate_step": "보통",
    "heartrate_ng": "3",
    "jayul_activity_score": "55.0",
    "jayul_activity_step": "나쁨",
    "piro_score": "57.0",
    "piro_step": "보통",
    "heart_stability_score": "51.3",
    "heart_stability_step": "보통",
    "jayul_balance_step": "54.8",
    "physical_stress_score": "56.1",
    "physical_stress_step": "보통",
    "mental_stress_score": "52.4",
    "mental_stress_step": "나쁨",
    "stress_ability_score": "54.9",
    "stress_ability_step": "나쁨",
    "total_grade": "55.2",
    "dongmaek_tansung_score": "53.9",
    "dongmaek_tansung_step": "나쁨",
    "malcho_tansung_score": "55.2",
    "malcho_tansung_step": "나쁨",
    "bloodvessel_age": "58",
    "bloodvessel_score": "63.0",
    "bloodvessel_step": "3",
    "bloodvessel_step_status": "나쁨",
    "datatime": "2024-07-22 13:00:00"
  },

  {
    "heartrate_avg": "66",
    "heartrate_score": "87.3",
    "heartrate_step": "좋음",
    "heartrate_ng": "0",
    "jayul_activity_score": "89.5",
    "jayul_activity_step": "매우좋음",
    "piro_score": "90.2",
    "piro_step": "매우좋음",
    "heart_stability_score": "84.1",
    "heart_stability_step": "좋음",
    "jayul_balance_step": "87.4",
    "physical_stress_score": "79.0",
    "physical_stress_step": "좋음",
    "mental_stress_score": "82.1",
    "mental_stress_step": "좋음",
    "stress_ability_score": "86.7",
    "stress_ability_step": "매우좋음",
    "total_grade": "90.0",
    "dongmaek_tansung_score": "85.1",
    "dongmaek_tansung_step": "좋음",
    "malcho_tansung_score": "89.0",
    "malcho_tansung_step": "매우좋음",
    "bloodvessel_age": "26",
    "bloodvessel_score": "94.2",
    "bloodvessel_step": "1",
    "bloodvessel_step_status": "매우좋음",
    "datatime": "2024-07-23 13:00:00"
  }
]
AL_DUMY= [
  {
    "alcohol_result": "PASS",
    "alcohol_yang": "0.00",
    "datatime": "2024-07-23 13:00:00"
  },
  {
    "alcohol_result": "PASS",
    "alcohol_yang": "0.01",
     "datatime": "2024-07-23 13:00:00"
  },
  {
    "alcohol_result": "PASS",
    "alcohol_yang": "0.02",
     "datatime": "2024-07-23 13:00:00"
  },
  {
    "alcohol_result": "PASS",
    "alcohol_yang": "0.03",
     "datatime": "2024-07-23 13:00:00"
  },
  {
    "alcohol_result": "FALL",
    "alcohol_yang": "0.04",
     "datatime": "2024-07-23 13:00:00"
  },
  {
    "alcohol_result": "FALL",
    "alcohol_yang": "0.05",
     "datatime": "2024-07-23 13:00:00"
  },
  {
    "alcohol_result": "FALL",
    "alcohol_yang": "0.08",
     "datatime": "2024-07-23 13:00:00"
  },
  {
    "alcohol_result": "FALL",
    "alcohol_yang": "0.12",
     "datatime": "2024-07-23 13:00:00"
  },
  {
    "alcohol_result": "FALL",
    "alcohol_yang": "0.18",
     "datatime": "2024-07-23 13:00:00"
  },
  {
    "alcohol_result": "FALL",
    "alcohol_yang": "0.22",
     "datatime": "2024-07-23 13:00:00"
  },
  {
    "alcohol_result": "FALL",
    "alcohol_yang": "0.30",
     "datatime": "2024-07-23 13:00:00"
  },
  {
    "alcohol_result": "FALL",
    "alcohol_yang": "0.35",
     "datatime": "2024-07-23 13:00:00"
  },
  {
    "alcohol_result": "FALL",
    "alcohol_yang": "0.42",
     "datatime": "2024-07-23 13:00:00"
  },
  {
    "alcohol_result": "FALL",
    "alcohol_yang": "0.55",
     "datatime": "2024-07-23 13:00:00"
  },
  {
    "alcohol_result": "FALL",
    "alcohol_yang": "0.63",
     "datatime": "2024-07-23 13:00:00"
  },
  {
    "alcohol_result": "FALL",
    "alcohol_yang": "0.78",
     "datatime": "2024-07-23 13:00:00"
  }
]


VA_DUMY= [
  {
    "left": "1.2",
    "left_status": "좌안정상",
    "right": "1.0",
    "right_status": "우안정상",
    "status": "VA 정상",
    "datatime": "2024-07-10 13:00:00"
  },
  {
    "left": "1.5",
    "left_status": "좌안정상",
    "right": "1.2",
    "right_status": "우안정상",
    "status": "VA 정상",
    "datatime": "2024-07-11 13:00:00"
  },
  {
    "left": "1.0",
    "left_status": "좌안정상",
    "right": "1.0",
    "right_status": "우안정상",
    "status": "VA 정상",
    "datatime": "2024-07-12 13:00:00"
  },
  {
    "left": "1.2",
    "left_status": "좌안정상",
    "right": "1.5",
    "right_status": "우안정상",
    "status": "VA 정상",
    "datatime": "2024-07-13 13:00:00"
  },
  {
    "left": "1.0",
    "left_status": "좌안정상",
    "right": "1.3",
    "right_status": "우안정상",
    "status": "VA 정상",
    "datatime": "2024-07-14 13:00:00"
  },

  {
    "left": "0.9",
    "left_status": "좌안주의",
    "right": "1.0",
    "right_status": "우안정상",
    "status": "VA 주의",
    "datatime": "2024-07-15 13:00:00"
  },
  {
    "left": "1.0",
    "left_status": "좌안정상",
    "right": "0.8",
    "right_status": "우안주의",
    "status": "VA 주의",
    "datatime": "2024-07-16 13:00:00"
  },
  {
    "left": "0.8",
    "left_status": "좌안주의",
    "right": "0.9",
    "right_status": "우안주의",
    "status": "VA 주의",
    "datatime": "2024-07-17 13:00:00"
  },
  {
    "left": "0.9",
    "left_status": "좌안주의",
    "right": "0.7",
    "right_status": "우안주의",
    "status": "VA 주의",
    "datatime": "2024-07-18 13:00:00"
  },
  {
    "left": "0.7",
    "left_status": "좌안주의",
    "right": "1.0",
    "right_status": "우안정상",
    "status": "VA 주의",
    "datatime": "2024-07-19 13:00:00"
  },

  {
    "left": "0.6",
    "left_status": "좌안저하",
    "right": "0.6",
    "right_status": "우안저하",
    "status": "VA 저하",
    "datatime": "2024-07-20 13:00:00"
  },
  {
    "left": "0.4",
    "left_status": "좌안저하",
    "right": "0.8",
    "right_status": "우안주의",
    "status": "VA 저하",
    "datatime": "2024-07-21 13:00:00"
  },
  {
    "left": "0.5",
    "left_status": "좌안저하",
    "right": "0.5",
    "right_status": "우안저하",
    "status": "VA 저하",
    "datatime": "2024-07-22 13:00:00"
  },
  {
    "left": "0.3",
    "left_status": "좌안저하",
    "right": "0.7",
    "right_status": "우안주의",
    "status": "VA 저하",
    "datatime": "2024-07-23 13:00:00"
  },
  {
    "left": "0.2",
    "left_status": "좌안저하",
    "right": "0.4",
    "right_status": "우안저하",
    "status": "VA 저하",
    "datatime": "2024-07-24 13:00:00"
  }
]


CM_DUMY= [
  {
    "value": "1",
    "datatime": "2024-07-10 13:00:00"
  },
  {
    "value": "2",
    "datatime": "2024-07-11 13:00:00"
  },
  {
    "value": "3",
    "datatime": "2024-07-12 13:00:00"
  },
  {
    "value": "1",
    "datatime": "2024-07-13 13:00:00"
  },
  {
    "value": "1",
    "datatime": "2024-07-14 13:00:00"
  },
  {
    "value": "2",
    "datatime": "2024-07-15 13:00:00"
  },
  {
    "value": "3",
    "datatime": "2024-07-16 13:00:00"
  },
  {
    "value": "1",
    "datatime": "2024-07-17 13:00:00"
  },
  {
    "value": "2",
    "datatime": "2024-07-18 13:00:00"
  },
  {
    "value": "3",
    "datatime": "2024-07-19 13:00:00"
  },
  {
    "value": "1",
    "datatime": "2024-07-20 13:00:00"
  },
  {
    "value": "2",
    "datatime": "2024-07-21 13:00:00"
  },
  {
    "value": "3",
    "datatime": "2024-07-22 13:00:00"
  },
  {
    "value": "1",
    "datatime": "2024-07-23 13:00:00"
  }
]

LU_DUMY= [
  {
    "valid_yn": "Y",
    "valid_idx": "0",
    "fvc_1": "3.80",
    "fvc_p_1": "3.90",
    "fev1_1": "3.10",
    "fev1_p_1": "3.20",
    "fev1fvc_1": "81.6",
    "fev1fvc_status_1": "정상",
    "fef2575_1": "3.20",
    "pef_1": "8.50",
    "pef_p_1": "8.80",
    "lung_age_1": "28",
    "fvc_2": "3.75",
    "fvc_p_2": "3.90",
    "fev1_2": "3.05",
    "fev1_p_2": "3.20",
    "fev1fvc_2": "81.3",
    "fev1fvc_status_2": "정상",
    "fef2575_2": "3.15",
    "pef_2": "8.40",
    "pef_p_2": "8.80",
    "lung_age_2": "29",
    "fvc_3": "3.70",
    "fvc_p_3": "3.90",
    "fev1_3": "3.00",
    "fev1_p_3": "3.20",
    "fev1fvc_3": "81.1",
    "fev1fvc_status_3": "정상",
    "fef2575_3": "3.10",
    "pef_3": "8.30",
    "pef_p_3": "8.80",
    "lung_age_3": "30",
    "datatime": "2024-07-10 13:00:00"
  },
  {
    "valid_yn": "Y",
    "valid_idx": "1",
    "fvc_1": "4.10",
    "fvc_p_1": "4.00",
    "fev1_1": "3.35",
    "fev1_p_1": "3.30",
    "fev1fvc_1": "81.7",
    "fev1fvc_status_1": "정상",
    "fef2575_1": "3.40",
    "pef_1": "8.90",
    "pef_p_1": "8.70",
    "lung_age_1": "26",
    "fvc_2": "4.05",
    "fvc_p_2": "4.00",
    "fev1_2": "3.30",
    "fev1_p_2": "3.30",
    "fev1fvc_2": "81.5",
    "fev1fvc_status_2": "정상",
    "fef2575_2": "3.38",
    "pef_2": "8.80",
    "pef_p_2": "8.70",
    "lung_age_2": "27",
    "fvc_3": "3.95",
    "fvc_p_3": "4.00",
    "fev1_3": "3.25",
    "fev1_p_3": "3.30",
    "fev1fvc_3": "82.3",
    "fev1fvc_status_3": "정상",
    "fef2575_3": "3.35",
    "pef_3": "8.60",
    "pef_p_3": "8.70",
    "lung_age_3": "28",
    "datatime": "2024-07-11 13:00:00"
  },
  {
    "valid_yn": "Y",
    "valid_idx": "2",
    "fvc_1": "3.50",
    "fvc_p_1": "3.80",
    "fev1_1": "2.80",
    "fev1_p_1": "3.10",
    "fev1fvc_1": "80.0",
    "fev1fvc_status_1": "정상",
    "fef2575_1": "2.90",
    "pef_1": "7.90",
    "pef_p_1": "8.50",
    "lung_age_1": "32",
    "fvc_2": "3.60",
    "fvc_p_2": "3.80",
    "fev1_2": "2.85",
    "fev1_p_2": "3.10",
    "fev1fvc_2": "79.2",
    "fev1fvc_status_2": "정상",
    "fef2575_2": "2.95",
    "pef_2": "8.00",
    "pef_p_2": "8.50",
    "lung_age_2": "33",
    "fvc_3": "3.70",
    "fvc_p_3": "3.80",
    "fev1_3": "2.95",
    "fev1_p_3": "3.10",
    "fev1fvc_3": "79.7",
    "fev1fvc_status_3": "정상",
    "fef2575_3": "3.00",
    "pef_3": "8.10",
    "pef_p_3": "8.50",
    "lung_age_3": "31",
    "datatime": "2024-07-12 13:00:00"
  },
  {
    "valid_yn": "Y",
    "valid_idx": "0",
    "fvc_1": "2.90",
    "fvc_p_1": "3.60",
    "fev1_1": "2.10",
    "fev1_p_1": "2.80",
    "fev1fvc_1": "72.4",
    "fev1fvc_status_1": "의심",
    "fef2575_1": "2.10",
    "pef_1": "6.90",
    "pef_p_1": "8.10",
    "lung_age_1": "45",
    "fvc_2": "2.95",
    "fvc_p_2": "3.60",
    "fev1_2": "2.15",
    "fev1_p_2": "2.80",
    "fev1fvc_2": "72.9",
    "fev1fvc_status_2": "의심",
    "fef2575_2": "2.15",
    "pef_2": "7.00",
    "pef_p_2": "8.10",
    "lung_age_2": "46",
    "fvc_3": "3.00",
    "fvc_p_3": "3.60",
    "fev1_3": "2.20",
    "fev1_p_3": "2.80",
    "fev1fvc_3": "73.3",
    "fev1fvc_status_3": "의심",
    "fef2575_3": "2.20",
    "pef_3": "7.10",
    "pef_p_3": "8.10",
    "lung_age_3": "44",
    "datatime": "2024-07-13 13:00:00"
  },
  {
    "valid_yn": "Y",
    "valid_idx": "1",
    "fvc_1": "3.10",
    "fvc_p_1": "3.50",
    "fev1_1": "2.40",
    "fev1_p_1": "2.90",
    "fev1fvc_1": "77.4",
    "fev1fvc_status_1": "정상",
    "fef2575_1": "2.50",
    "pef_1": "7.40",
    "pef_p_1": "8.00",
    "lung_age_1": "38",
    "fvc_2": "3.20",
    "fvc_p_2": "3.50",
    "fev1_2": "2.50",
    "fev1_p_2": "2.90",
    "fev1fvc_2": "78.1",
    "fev1fvc_status_2": "정상",
    "fef2575_2": "2.60",
    "pef_2": "7.60",
    "pef_p_2": "8.00",
    "lung_age_2": "37",
    "fvc_3": "3.05",
    "fvc_p_3": "3.50",
    "fev1_3": "2.35",
    "fev1_p_3": "2.90",
    "fev1fvc_3": "77.0",
    "fev1fvc_status_3": "정상",
    "fef2575_3": "2.45",
    "pef_3": "7.30",
    "pef_p_3": "8.00",
    "lung_age_3": "39",
    "datatime": "2024-07-14 13:00:00"
  },
  {
    "valid_yn": "N",
    "valid_idx": "2",
    "fvc_1": "2.50",
    "fvc_p_1": "3.40",
    "fev1_1": "1.80",
    "fev1_p_1": "2.70",
    "fev1fvc_1": "72.0",
    "fev1fvc_status_1": "의심",
    "fef2575_1": "1.90",
    "pef_1": "6.20",
    "pef_p_1": "7.90",
    "lung_age_1": "58",
    "fvc_2": "2.60",
    "fvc_p_2": "3.40",
    "fev1_2": "1.85",
    "fev1_p_2": "2.70",
    "fev1fvc_2": "71.2",
    "fev1fvc_status_2": "의심",
    "fef2575_2": "1.95",
    "pef_2": "6.40",
    "pef_p_2": "7.90",
    "lung_age_2": "59",
    "fvc_3": "2.55",
    "fvc_p_3": "3.40",
    "fev1_3": "1.80",
    "fev1_p_3": "2.70",
    "fev1fvc_3": "70.6",
    "fev1fvc_status_3": "의심",
    "fef2575_3": "1.92",
    "pef_3": "6.30",
    "pef_p_3": "7.90",
    "lung_age_3": "60",
    "datatime": "2024-07-15 13:00:00"
  },
  {
    "valid_yn": "Y",
    "valid_idx": "0",
    "fvc_1": "4.30",
    "fvc_p_1": "4.20",
    "fev1_1": "3.60",
    "fev1_p_1": "3.50",
    "fev1fvc_1": "83.7",
    "fev1fvc_status_1": "정상",
    "fef2575_1": "3.70",
    "pef_1": "9.10",
    "pef_p_1": "8.90",
    "lung_age_1": "25",
    "fvc_2": "4.25",
    "fvc_p_2": "4.20",
    "fev1_2": "3.55",
    "fev1_p_2": "3.50",
    "fev1fvc_2": "83.5",
    "fev1fvc_status_2": "정상",
    "fef2575_2": "3.65",
    "pef_2": "9.00",
    "pef_p_2": "8.90",
    "lung_age_2": "24",
    "fvc_3": "4.20",
    "fvc_p_3": "4.20",
    "fev1_3": "3.50",
    "fev1_p_3": "3.50",
    "fev1fvc_3": "83.3",
    "fev1fvc_status_3": "정상",
    "fef2575_3": "3.60",
    "pef_3": "8.95",
    "pef_p_3": "8.90",
    "lung_age_3": "23",
    "datatime": "2024-07-16 13:00:00"
  },
  {
    "valid_yn": "Y",
    "valid_idx": "1",
    "fvc_1": "3.30",
    "fvc_p_1": "3.60",
    "fev1_1": "2.60",
    "fev1_p_1": "3.00",
    "fev1fvc_1": "78.8",
    "fev1fvc_status_1": "정상",
    "fef2575_1": "2.70",
    "pef_1": "7.50",
    "pef_p_1": "8.20",
    "lung_age_1": "36",
    "fvc_2": "3.40",
    "fvc_p_2": "3.60",
    "fev1_2": "2.70",
    "fev1_p_2": "3.00",
    "fev1fvc_2": "79.4",
    "fev1fvc_status_2": "정상",
    "fef2575_2": "2.80",
    "pef_2": "7.70",
    "pef_p_2": "8.20",
    "lung_age_2": "35",
    "fvc_3": "3.35",
    "fvc_p_3": "3.60",
    "fev1_3": "2.65",
    "fev1_p_3": "3.00",
    "fev1fvc_3": "79.1",
    "fev1fvc_status_3": "정상",
    "fef2575_3": "2.75",
    "pef_3": "7.60",
    "pef_p_3": "8.20",
    "lung_age_3": "37",
    "datatime": "2024-07-17 13:00:00"
  },
  {
    "valid_yn": "N",
    "valid_idx": "0",
    "fvc_1": "2.30",
    "fvc_p_1": "3.20",
    "fev1_1": "1.60",
    "fev1_p_1": "2.50",
    "fev1fvc_1": "69.6",
    "fev1fvc_status_1": "의심",
    "fef2575_1": "1.70",
    "pef_1": "5.90",
    "pef_p_1": "7.50",
    "lung_age_1": "62",
    "fvc_2": "2.40",
    "fvc_p_2": "3.20",
    "fev1_2": "1.65",
    "fev1_p_2": "2.50",
    "fev1fvc_2": "68.8",
    "fev1fvc_status_2": "의심",
    "fef2575_2": "1.75",
    "pef_2": "6.00",
    "pef_p_2": "7.50",
    "lung_age_2": "63",
    "fvc_3": "2.35",
    "fvc_p_3": "3.20",
    "fev1_3": "1.60",
    "fev1_p_3": "2.50",
    "fev1fvc_3": "68.1",
    "fev1fvc_status_3": "의심",
    "fef2575_3": "1.72",
    "pef_3": "5.95",
    "pef_p_3": "7.50",
    "lung_age_3": "61",
    "datatime": "2024-07-18 13:00:00"
  },
  {
    "valid_yn": "Y",
    "valid_idx": "2",
    "fvc_1": "3.90",
    "fvc_p_1": "4.00",
    "fev1_1": "3.10",
    "fev1_p_1": "3.30",
    "fev1fvc_1": "79.5",
    "fev1fvc_status_1": "정상",
    "fef2575_1": "3.20",
    "pef_1": "8.40",
    "pef_p_1": "8.70",
    "lung_age_1": "31",
    "fvc_2": "3.95",
    "fvc_p_2": "4.00",
    "fev1_2": "3.15",
    "fev1_p_2": "3.30",
    "fev1fvc_2": "79.7",
    "fev1fvc_status_2": "정상",
    "fef2575_2": "3.25",
    "pef_2": "8.50",
    "pef_p_2": "8.70",
    "lung_age_2": "30",
    "fvc_3": "4.00",
    "fvc_p_3": "4.00",
    "fev1_3": "3.20",
    "fev1_p_3": "3.30",
    "fev1fvc_3": "80.0",
    "fev1fvc_status_3": "정상",
    "fef2575_3": "3.30",
    "pef_3": "8.60",
    "pef_p_3": "8.70",
    "lung_age_3": "29",
    "datatime": "2024-07-19 13:00:00"
  },
  {
    "valid_yn": "Y",
    "valid_idx": "1",
    "fvc_1": "3.20",
    "fvc_p_1": "3.40",
    "fev1_1": "2.60",
    "fev1_p_1": "2.90",
    "fev1fvc_1": "81.3",
    "fev1fvc_status_1": "정상",
    "fef2575_1": "2.70",
    "pef_1": "7.60",
    "pef_p_1": "8.00",
    "lung_age_1": "34",
    "fvc_2": "3.25",
    "fvc_p_2": "3.40",
    "fev1_2": "2.65",
    "fev1_p_2": "2.90",
    "fev1fvc_2": "81.5",
    "fev1fvc_status_2": "정상",
    "fef2575_2": "2.75",
    "pef_2": "7.70",
    "pef_p_2": "8.00",
    "lung_age_2": "33",
    "fvc_3": "3.15",
    "fvc_p_3": "3.40",
    "fev1_3": "2.55",
    "fev1_p_3": "2.90",
    "fev1fvc_3": "81.0",
    "fev1fvc_status_3": "정상",
    "fef2575_3": "2.65",
    "pef_3": "7.50",
    "pef_p_3": "8.00",
    "lung_age_3": "35",
    "datatime": "2024-07-20 13:00:00"
  },
  {
    "valid_yn": "Y",
    "valid_idx": "0",
    "fvc_1": "3.00",
    "fvc_p_1": "3.30",
    "fev1_1": "2.40",
    "fev1_p_1": "2.80",
    "fev1fvc_1": "80.0",
    "fev1fvc_status_1": "정상",
    "fef2575_1": "2.50",
    "pef_1": "7.20",
    "pef_p_1": "7.90",
    "lung_age_1": "40",
    "fvc_2": "2.95",
    "fvc_p_2": "3.30",
    "fev1_2": "2.35",
    "fev1_p_2": "2.80",
    "fev1fvc_2": "79.7",
    "fev1fvc_status_2": "정상",
    "fef2575_2": "2.45",
    "pef_2": "7.10",
    "pef_p_2": "7.90",
    "lung_age_2": "41",
    "fvc_3": "3.05",
    "fvc_p_3": "3.30",
    "fev1_3": "2.45",
    "fev1_p_3": "2.80",
    "fev1fvc_3": "80.3",
    "fev1fvc_status_3": "정상",
    "fef2575_3": "2.55",
    "pef_3": "7.30",
    "pef_p_3": "7.90",
    "lung_age_3": "39",
    "datatime": "2024-07-21 13:00:00"
  },
  {
    "valid_yn": "N",
    "valid_idx": "2",
    "fvc_1": "2.60",
    "fvc_p_1": "3.30",
    "fev1_1": "1.90",
    "fev1_p_1": "2.70",
    "fev1fvc_1": "73.1",
    "fev1fvc_status_1": "의심",
    "fef2575_1": "2.00",
    "pef_1": "6.40",
    "pef_p_1": "7.80",
    "lung_age_1": "55",
    "fvc_2": "2.70",
    "fvc_p_2": "3.30",
    "fev1_2": "1.95",
    "fev1_p_2": "2.70",
    "fev1fvc_2": "72.2",
    "fev1fvc_status_2": "의심",
    "fef2575_2": "2.05",
    "pef_2": "6.50",
    "pef_p_2": "7.80",
    "lung_age_2": "56",
    "fvc_3": "2.65",
    "fvc_p_3": "3.30",
    "fev1_3": "1.90",
    "fev1_p_3": "2.70",
    "fev1fvc_3": "71.7",
    "fev1fvc_status_3": "의심",
    "fef2575_3": "2.02",
    "pef_3": "6.45",
    "pef_p_3": "7.80",
    "lung_age_3": "54",
    "datatime": "2024-07-22 13:00:00"
  },
  {
    "valid_yn": "Y",
    "valid_idx": "1",
    "fvc_1": "3.60",
    "fvc_p_1": "3.80",
    "fev1_1": "2.90",
    "fev1_p_1": "3.10",
    "fev1fvc_1": "80.6",
    "fev1fvc_status_1": "정상",
    "fef2575_1": "3.00",
    "pef_1": "8.00",
    "pef_p_1": "8.40",
    "lung_age_1": "33",
    "fvc_2": "3.65",
    "fvc_p_2": "3.80",
    "fev1_2": "2.95",
    "fev1_p_2": "3.10",
    "fev1fvc_2": "80.8",
    "fev1fvc_status_2": "정상",
    "fef2575_2": "3.05",
    "pef_2": "8.10",
    "pef_p_2": "8.40",
    "lung_age_2": "32",
    "fvc_3": "3.55",
    "fvc_p_3": "3.80",
    "fev1_3": "2.85",
    "fev1_p_3": "3.10",
    "fev1fvc_3": "80.3",
    "fev1fvc_status_3": "정상",
    "fef2575_3": "2.95",
    "pef_3": "7.90",
    "pef_p_3": "8.40",
    "lung_age_3": "34",
    "datatime": "2024-07-23 13:00:00"
  },
  {
    "valid_yn": "Y",
    "valid_idx": "0",
    "fvc_1": "3.40",
    "fvc_p_1": "3.70",
    "fev1_1": "2.70",
    "fev1_p_1": "3.00",
    "fev1fvc_1": "81.0",
    "fev1fvc_status_1": "정상",
    "fef2575_1": "2.80",
    "pef_1": "7.80",
    "pef_p_1": "8.20",
    "lung_age_1": "35",
    "fvc_2": "3.45",
    "fvc_p_2": "3.70",
    "fev1_2": "2.75",
    "fev1_p_2": "3.00",
    "fev1fvc_2": "79.7",
    "fev1fvc_status_2": "정상",
    "fef2575_2": "2.85",
    "pef_2": "7.90",
    "pef_p_2": "8.20",
    "lung_age_2": "36",
    "fvc_3": "3.35",
    "fvc_p_3": "3.70",
    "fev1_3": "2.65",
    "fev1_p_3": "3.00",
    "fev1fvc_3": "79.1",
    "fev1fvc_status_3": "정상",
    "fef2575_3": "2.75",
    "pef_3": "7.70",
    "pef_p_3": "8.20",
    "lung_age_3": "34",
    "datatime": "2024-07-24 13:00:00"
  }
]


BS_DUMY= [
  {
    "status": "정상",
    "bloodsugar_type": "식전",
    "bloodsugar": "92",
    "col_total": "178",
    "col_tri": "95",
    "col_ldl": "104",
    "col_hdl": "58",
    "datatime": "2024-07-10 13:00:00"
  },
  {
    "status": "정상",
    "bloodsugar_type": "식전",
    "bloodsugar": "88",
    "col_total": "170",
    "col_tri": "88",
    "col_ldl": "98",
    "col_hdl": "62",
    "datatime": "2024-07-11 13:00:00"
  },
  {
    "status": "정상",
    "bloodsugar_type": "식후",
    "bloodsugar": "118",
    "col_total": "182",
    "col_tri": "110",
    "col_ldl": "106",
    "col_hdl": "55",
    "datatime": "2024-07-12 13:00:00"
  },
  {
    "status": "주의",
    "bloodsugar_type": "식전",
    "bloodsugar": "108",
    "col_total": "196",
    "col_tri": "135",
    "col_ldl": "122",
    "col_hdl": "49",
    "datatime": "2024-07-13 13:00:00"
  },
  {
    "status": "주의",
    "bloodsugar_type": "식후",
    "bloodsugar": "142",
    "col_total": "205",
    "col_tri": "148",
    "col_ldl": "128",
    "col_hdl": "46",
    "datatime": "2024-07-14 13:00:00"
  },
  {
    "status": "정상",
    "bloodsugar_type": "식전",
    "bloodsugar": "95",
    "col_total": "175",
    "col_tri": "90",
    "col_ldl": "101",
    "col_hdl": "60",
    "datatime": "2024-07-15 13:00:00"
  },
  {
    "status": "주의",
    "bloodsugar_type": "식후",
    "bloodsugar": "155",
    "col_total": "214",
    "col_tri": "160",
    "col_ldl": "135",
    "col_hdl": "43",
    "datatime": "2024-07-16 13:00:00"
  },
  {
    "status": "위험",
    "bloodsugar_type": "식전",
    "bloodsugar": "132",
    "col_total": "228",
    "col_tri": "182",
    "col_ldl": "146",
    "col_hdl": "40",
    "datatime": "2024-07-17 13:00:00"
  },
  {
    "status": "위험",
    "bloodsugar_type": "식후",
    "bloodsugar": "189",
    "col_total": "240",
    "col_tri": "210",
    "col_ldl": "158",
    "col_hdl": "37",
    "datatime": "2024-07-18 13:00:00"
  },
  {
    "status": "주의",
    "bloodsugar_type": "식전",
    "bloodsugar": "115",
    "col_total": "202",
    "col_tri": "140",
    "col_ldl": "126",
    "col_hdl": "48",
    "datatime": "2024-07-19 13:00:00"
  },
  {
    "status": "정상",
    "bloodsugar_type": "식후",
    "bloodsugar": "124",
    "col_total": "188",
    "col_tri": "120",
    "col_ldl": "110",
    "col_hdl": "53",
    "datatime": "2024-07-20 13:00:00"
  },
  {
    "status": "정상",
    "bloodsugar_type": "식전",
    "bloodsugar": "90",
    "col_total": "172",
    "col_tri": "92",
    "col_ldl": "100",
    "col_hdl": "61",
    "datatime": "2024-07-21 13:00:00"
  },
  {
    "status": "주의",
    "bloodsugar_type": "식후",
    "bloodsugar": "160",
    "col_total": "218",
    "col_tri": "170",
    "col_ldl": "140",
    "col_hdl": "42",
    "datatime": "2024-07-22 13:00:00"
  },
  {
    "status": "위험",
    "bloodsugar_type": "식전",
    "bloodsugar": "140",
    "col_total": "252",
    "col_tri": "230",
    "col_ldl": "172",
    "col_hdl": "35",
    "datatime": "2024-07-23 13:00:00"
  }
]




# -----------------------------
# 데이터 클래스 정의
# -----------------------------


@dataclass
class AuthUserRequest:
    userid: str
    token: str
    type: str = "PHONE"
    serviceforce: str = "false"  # 서버에서 문자열을 요구함

@dataclass
class AuthGetTokenRequest:
    kioskid: str


@dataclass
class SetResultRequest:
    token: str
    measureid: str
    device: str
    result: any
    serviceforce: str = "false"


# -----------------------------
# API 호출 함수
# -----------------------------


def get_api_token(kioskid: str) -> str:
  
  url = BASE_URL + AUTH_GET_TOKEN_PATH
  req = AuthGetTokenRequest(kioskid=kioskid)
  
  resp = requests.post(url, json=asdict(req), timeout=5)
  resp.raise_for_status()
  
  data = resp.json()
  
  if data.get("resultCode") != 200:
        raise RuntimeError(f"api-token 실패: {data}")
  
  token = data["resultData"]["token"]
  print(f"토큰: {token}")
  
  return token
  


def send_auth_user(user_phone: str,token:str) -> str:
    """/api/auth-user 호출 → measureid 반환"""
    url = BASE_URL + AUTH_USER_PATH

    req = AuthUserRequest(
        userid=user_phone,
        token=token,
    )

    resp = requests.post(url, json=asdict(req), headers=HEADERS, timeout=5)
    # print("[auth-user] status:", resp.status_code)

    resp.raise_for_status()
    data = resp.json()

    if data.get("resultCode") != 200:
        raise RuntimeError(f"auth-user 실패: {data}")

    measureid = data["resultData"]["measureid"]
    # print("[auth-user] measureid:", measureid)

    return measureid


def send_set_result(token:str,measureid: str, result, device_code: str):
    """/api/set-result 호출"""
    url = BASE_URL + SET_RESULT_PATH

    req = SetResultRequest(
        token=token,
        measureid=measureid,
        device=device_code,
        result=result,
        serviceforce="false",
    )

    body = asdict(req)
    resp = requests.post(url, json=body, headers=HEADERS, timeout=5)
    time.sleep(0.5)
    print("[set-result] status:", resp.status_code)

    try:
        print("[set-result] response:", resp.json())
    except:
        print("[set-result] raw:", resp.text)

    resp.raise_for_status()





def send_start(data_list: list, device_code: str):
    for i, data in enumerate(data_list, start=1):
        print(f"\n===== #{device_code}_{i} 개 저장 시작 =====")

        
        measureid_1 = send_auth_user(user_phone=USER_PHONE_1)
        measureid_2 = send_auth_user(user_phone=USER_PHONE_2)
        measureid_3 = send_auth_user(user_phone=USER_PHONE_3)
        measureid_4 = send_auth_user(user_phone=USER_PHONE_4)
        measureid_5 = send_auth_user(user_phone=USER_PHONE_5)
        

      
        send_set_result(measureid_1, data,device_code=device_code)
        send_set_result(measureid_2, data,device_code=device_code)
        send_set_result(measureid_3, data,device_code=device_code)
        send_set_result(measureid_4, data,device_code=device_code)
        send_set_result(measureid_5, data,device_code=device_code)
        

    # print("\n=== 모든 샘플 데이터 저장 완료 ===")
    






def main():
    print("====토큰 발급 시작====")
    api_token = get_api_token(kioskid=KIOSK_ID)
    if api_token:
      print("====토큰 발급 완료====")
      # print("=== BP 데이터 저장 시작 ===")
      # send_start(BP_DUMY, device_code=BP)
      # print("=== BP 데이터 저장 끝===")
      # print("=== HS 데이터 저장 시작 ===")
      # send_start(HS_DUMY, device_code=HS)
      # print("=== HS 데이터 저장 끝 ===")
      # print("=== BC 데이터 저장 시작 ===")
      # send_start(BC_DUMY, device_code=BC)
      # print("=== BC 데이터 저장 끝 ===")
      # print("=== ST 데이터 저장 시작 ===")
      # send_start(ST_DUMY, device_code=ST)
      # print("=== ST 데이터 저장 끝 ===")
      # print("=== LU 데이터 저장 시작 ===")
      # send_start(LU_DUMY, device_code=LU)
      # print("=== LU 데이터 저장 끝 ===")
      # print("=== BS 데이터 저장 시작 ===")
      # send_start(BS_DUMY, device_code=BS)
      # print("=== BS 데이터 저장 끝 ===")
      # print("=== AL 데이터 저장 시작 ===")
      # send_start(AL_DUMY, device_code=AL)
      # print("=== AL 데이터 저장 끝 ===")
      # print("=== BC 데이터 저장 시작 ===")
      # send_start(BC_DUMY, device_code=BC)
      # print("=== BC 데이터 저장 끝 ===")
      # print("=== CM 데이터 저장 시작 ===")
      # send_start(CM_DUMY, device_code=CM)
      # print("=== CM 데이터 저장 끝 ===")
      # print("===VA 데이터 저장 시작 ===")
      # send_start(VA_DUMY, device_code=VA)
      # print("=== VA 데이터 저장 끝 ===")
    



if __name__ == "__main__":
    main()
