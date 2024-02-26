import os

script_dir = os.path.dirname(os.path.abspath(__file__))
print(script_dir)
print(os.path.exists(script_dir))
common_parent_dir = os.path.abspath(os.path.join(script_dir, '..'))
true_folder = os.path.abspath(os.path.join(common_parent_dir, '..'))
output_folder_path = os.path.join(script_dir, 'media', 'uploads')
print(output_folder_path)



host_audio_path = os.path.join(output_folder_path, 'Untitled spreadsheet - Sheet1(1).csv')
print(host_audio_path)