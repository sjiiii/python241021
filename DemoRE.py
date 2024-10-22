#DemoRE
#정규표현식 사용

import re

Result = re.search("[0-9]*th", "  35th")
print(Result)
print(Result.group())

# result2 = re.match("[0-9]*th", "  35th")
# print(result2)
# print(result2.group())      

result3 = re.search("ap", "This is apple")
print(result3.group())

result4 = re.search("\d{4}", "올해는 2024년입니다.")
print(result4.group())      

result5 = re.search("\d{5}", "우리동네는 52300")
print(result5.group())





def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.search(pattern, email))

# 테스트 샘플
test_emails = [
    "user@example.com",
    "user.name@example.co.kr",
    "user+tag@example.org",
    "user123@sub.example.com",
    "user@example",  # 잘못된 이메일
    "user@.com",  # 잘못된 이메일
    "user@example.",  # 잘못된 이메일
    "@example.com",  # 잘못된 이메일
    "user@example_com",  # 잘못된 이메일
    "한글사용자@example.com",  # 한글 포함
]

# 테스트 실행
for email in test_emails:
    if is_valid_email(email):
        print(f"{email}: 유효한 이메일 주소입니다.")
    else:
        print(f"{email}: 유효하지 않은 이메일 주소입니다.")
