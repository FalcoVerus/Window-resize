import pygetwindow as pygw
import pandas as pd

def list_open_windows():
    windows = pygw.getAllTitles()
    window_props = ['Name', 'Width', 'Height', 'Left', 'Top']
    windowdf = pd.DataFrame(columns=window_props)
    for window_title in windows:
        window = pygw.getWindowsWithTitle(window_title)[0]
        if window.width > 1 and window.title != "Program Manager" and window.title != 'Settings':
            if 'Brave' in window.title and window.left < 500:
                window_name = 'Brave#1'
            elif 'Brave' in window.title and window.left > 500:
                  window_name = 'Brave#2'
            elif 'Total Commander' in window.title:
                window_name = 'Total Commander'
            elif 'Visual Studio Code' in window.title:
                window_name = 'Visual Studio Code'
            elif 'Thunderbird' in window.title:
                window_name = 'Thunderbird'
            elif 'Discord' in window.title:
                window_name = 'Discord'
            elif 'Outlook' in window.title:
                window_name = 'Outlook'
            elif 'Slack' in window.title:
                window_name = 'Slack'
            else:
                window_name = 'File Explorer'
            windowdf_append = {'Name': window_name, 'Width': window.width, 'Height': window.height, 'Left': window.left, 'Top': window.top}
            windowdf.loc[len(windowdf)] = windowdf_append
    print(windowdf)
    windowdf.to_csv('Running_windows.csv', index=False)

def restore_open_windows():
    input_file = input('Enter the name of the .csv file with the saved window data: ')
    windowdf = pd.read_csv(input_file)
    windowdf.set_index('Name', inplace=True)
    windows = pygw.getAllTitles()
    count = 0
    for window_title in windows:
        window = pygw.getWindowsWithTitle(window_title)[0]
        if window.width > 1 and window.title != "Program Manager" and window.title != 'Settings':
            if 'Brave' in window.title and count == 0:
                window_name = 'Brave#1'
                window.moveTo(int(windowdf.loc[window_name, 'Left']), int(windowdf.loc[window_name, 'Top']))
                window.resizeTo(int(windowdf.loc[window_name, 'Width']), int(windowdf.loc[window_name, 'Height']))
                count = 1
            elif 'Brave' in window.title and count > 0:
                window_name = 'Brave#2'
                window.moveTo(int(windowdf.loc[window_name, 'Left']), int(windowdf.loc[window_name, 'Top']))
                window.resizeTo(int(windowdf.loc[window_name, 'Width']), int(windowdf.loc[window_name, 'Height']))
            elif 'Total Commander' in window.title:
                window_name = 'Total Commander'
                window.moveTo(int(windowdf.loc[window_name, 'Left']), int(windowdf.loc[window_name, 'Top']))
                window.resizeTo(int(windowdf.loc[window_name, 'Width']), int(windowdf.loc[window_name, 'Height']))
            elif 'Visual Studio Code' in window.title:
                window_name = 'Visual Studio Code'
                window.moveTo(int(windowdf.loc[window_name, 'Left']), int(windowdf.loc[window_name, 'Top']))
                window.resizeTo(int(windowdf.loc[window_name, 'Width']), int(windowdf.loc[window_name, 'Height']))
            elif 'Thunderbird' in window.title:
                window_name = 'Thunderbird'
                window.moveTo(int(windowdf.loc[window_name, 'Left']), int(windowdf.loc[window_name, 'Top']))
                window.resizeTo(int(windowdf.loc[window_name, 'Width']), int(windowdf.loc[window_name, 'Height']))
            elif 'Discord' in window.title:
                window_name = 'Discord'
                window.moveTo(int(windowdf.loc[window_name, 'Left']), int(windowdf.loc[window_name, 'Top']))
                window.resizeTo(int(windowdf.loc[window_name, 'Width']), int(windowdf.loc[window_name, 'Height']))
            elif 'Outlook' in window.title:
                window_name = 'Outlook'
                window.moveTo(int(windowdf.loc[window_name, 'Left']), int(windowdf.loc[window_name, 'Top']))
                window.resizeTo(int(windowdf.loc[window_name, 'Width']), int(windowdf.loc[window_name, 'Height']))
            elif 'Slack' in window.title:
                window_name = 'Slack'
                window.moveTo(int(windowdf.loc[window_name, 'Left']), int(windowdf.loc[window_name, 'Top']))
                window.resizeTo(int(windowdf.loc[window_name, 'Width']), int(windowdf.loc[window_name, 'Height']))
            else:
                window_name = 'File Explorer'
                window.moveTo(int(windowdf.loc[window_name, 'Left']), int(windowdf.loc[window_name, 'Top']))
                window.resizeTo(int(windowdf.loc[window_name, 'Width']), int(windowdf.loc[window_name, 'Height']))

if __name__ == "__main__":
    io = input('Do you want to save (1) or restore (2) your windows?: ')
    if io == '1':
        list_open_windows()
    elif io == '2':
        restore_open_windows()
    else:
        print('Invalid input, please specify 1 or 2!')