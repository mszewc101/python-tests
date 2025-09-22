s = 'Python'
s = list(s)
s.reverse()
print(s)
 
final_string = "".join(s)
print(f"Moj ciag znakow to {final_string}")

path_to_file_windows = 'C:\Repositories\codebrainers_2025_07'
path_to_file_linux = 'C:/Repositories/codebrainers_2025_07'
print(path_to_file_windows, path_to_file_linux)

path_to_file_list = ('C:', 'Repositories', 'codebrainers_2025_07')
changed_path = '\\'.join(path_to_file_list)
print(f"Final path: {changed_path}")