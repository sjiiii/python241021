import os
import shutil

# 다운로드 폴더 경로
download_folder = r"C:\Users\student\Downloads"

# 이동할 폴더 경로
image_folder = os.path.join(download_folder, 'images')
data_folder = os.path.join(download_folder, 'data')
docs_folder = os.path.join(download_folder, 'docs')
archive_folder = os.path.join(download_folder, 'archive')

# 이동할 폴더가 없으면 생성
os.makedirs(image_folder, exist_ok=True)
os.makedirs(data_folder, exist_ok=True)
os.makedirs(docs_folder, exist_ok=True)
os.makedirs(archive_folder, exist_ok=True)

# 확장자별로 파일을 이동
def move_files_by_extension(extension_list, destination_folder):
    for filename in os.listdir(download_folder):
        # 파일 확장자가 조건에 맞는지 확인
        if filename.lower().endswith(extension_list):
            source = os.path.join(download_folder, filename)
            destination = os.path.join(destination_folder, filename)
            print(f"Moving {source} to {destination}")
            shutil.move(source, destination)  # 파일 이동

# 각 파일 형식에 맞는 폴더로 이동
move_files_by_extension(('.jpg', '.jpeg'), image_folder)
move_files_by_extension(('.csv', '.xlsx'), data_folder)
move_files_by_extension(('.txt', '.doc', '.pdf'), docs_folder)
move_files_by_extension(('.zip',), archive_folder)

print("파일 정리가 완료되었습니다.")
