import os
import sys
from main import os_run
from utils import configure

"""
//
// Copyright 2022 CPVS & Lenovo C-Cay Inc.
//
// HTML <H5> and JavaScript <JS> and corresponding source code is free
// software: you can redistribute it and/or modify it under the terms of
// the GNU General Public License as published by the Free Software Foundation,
// either version 3 of the License, or (at your option) any later version.

// HTML <H5> and JavaScript <JS> and corresponding source code is distributed
// in the hope that it will be useful, but with permitted additional restrictions
// under Section 7 of the GPL. See the GNU General Public License in LICENSE.TXT
// distributed with this program. You should have received a copy of the
// GNU General Public License along with permitted additional restrictions
// with this program. If not, see #todo GitHub Url for the location of the GNU

/* $Header: /Code/main.py 1     08/08/22 00:00a C-Cay Bing_John $ */
/***********************************************************************************************
 ***              C O N F I D E N T I A L  ---  L E N O V O & C - C A Y  S T U D I O S       ***
 ***********************************************************************************************
 *                                                                                             *
 *                 Project Name : Attendance & Procedure                                       *
 *                                                                                             *
 *                    File Name : Run.py                                                       *
 *                                                                                             *
 *                   Programmer : Joe L. Bing_John                                             *
 *                                                                                             *
 *                   Start Date : June 30, 2022                                                *
 *                                                                                             *
 *                  Last Update : August 20, 2022 [JLB]                                        *
 *                                                                                             *
 *---------------------------------------------------------------------------------------------*
  * Functions:                                                                                 *
 *   earch -- None                                                                             *
 * - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */
"""

"""
/***********************************************************************************************
 * Search & Corfolder -- Query the folder of the current program running directory             *
 *                                                                                             *
 *                                                                                             *
 *                                                                                             *
 * INPUT:    Folder, File_name                                                                 *
 *                                                                                             *
 * OUTPUT:   Folder Path                                                                       *
 *                                                                                             *
 * WARNINGS: None                                                                              *
 *                                                                                             *
 * HISTORY:                                                                                    *
 *    30/06/22 13:00AM ST : Created                                                            *
 *=============================================================================================*/
"""


def search_corfolder(folder, file_name):
    # noinspection PyBroadException
    try:
        files = os.listdir(folder)
    except:
        # print(f'{folder} : NUll ??????????????????')
        return None

    if files.__contains__(file_name):
        return os.path.join(folder, file_name)
    else:
        # ???????????????
        return None


"""
/***********************************************************************************************
 * Search & Allfolder -- Query all folders of the current disk formation                       *
 *                                                                                             *
 *                                                                                             *
 *                                                                                             *
 * INPUT:    Folder, File_name                                                                 *
 *                                                                                             *
 * OUTPUT:   Folder Path                                                                       *
 *                                                                                             *
 * WARNINGS: None                                                                              *
 *                                                                                             *
 * HISTORY:                                                                                    *
 *    30/06/22 13:38AM ST : Created                                                            *
 *=============================================================================================*/
"""


def search_allfolder(folder, file_name):
    file_path = search_corfolder(folder, file_name)
    if file_path:
        return file_path
    else:
        # noinspection PyBroadException
        try:
            files = os.listdir(folder)
        except:
            return None
        folders = list(map(lambda name: folder + '\\' + name, filter(lambda paths: not paths.__contains__('.'), files)))
        if not folders:
            return None
        for folder_path in folders:
            if os.path.isdir(folder_path):
                file_path = search_allfolder(folder_path, file_name)
                if file_path:
                    return file_path
    return None


"""
/***********************************************************************************************
 * Search -- Query the entire current folder and its subfolders                                *                                                 *
 *                                                                                             *
 *                                                                                             *
 *                                                                                             *
 * INPUT:    Sys_path, Sys_name, model='current'                                               *
 *                                                                                             *
 * OUTPUT:   Folder Path                                                                       *
 *                                                                                             *
 * WARNINGS: all or usa                                                                        *
 *                                                                                             *
 * HISTORY:                                                                                    *
 *    30/06/22 13:54AM ST : Created                                                            *
 *=============================================================================================*/
"""


def search(sys_path, sys_name, model='current'):
    def search_info(folder, file_name):
        if model == 'all':
            file_path = search_allfolder(folder, file_name)
            return file_path

        if model == 'usa':
            file_path = search_corfolder(folder, file_name)
            return file_path

    # ?????????????????? all:??????????????? usa:??????????????????

    try:
        if not sys_path:
            # ???????????? sys_path ??? sys_name ???????????? search_info()???
            return search_info(sys_path, sys_name)
        else:
            return 'False'

    except Exception as e:
        return f'{e}'

    # ?????????????????? ????????????????????????


"""
/***********************************************************************************************
 * Search -- Path Query the current path                                                       *                                                 *
 *                                                                                             *
 *                                                                                             *
 *                                                                                             *
 * INPUT:    Nothing                                                                           *
 *                                                                                             *
 * OUTPUT:   Folder Path                                                                       *
 *                                                                                             *
 * WARNINGS: all or usa                                                                        *
 *                                                                                             *
 * HISTORY:                                                                                    *
 *    30/06/22 13:54AM ST : Created                                                            *
 *=============================================================================================*/
"""


# noinspection PyBroadException
def search_path():
    # # sys_path = os.path.abspath('.')[:3]
    #     # ?????? configure.py ????????????????????????????????? ini() ?????????
    #     ini_path = user_configure.ini()['usall']
    # sys_path = os.path.abspath('.')[:3]
    # ?????? configure.py ????????????????????????????????? ini() ?????????
    ini_path = configure.ini()['usall']

    for i in ini_path:
        sys.path.append(os.path.abspath(f'{i}'))

        # ?????? sys ??????????????????

    os_run()  # ??????????????????????????? ?????? APP [Flask] ??????

    # ???????????????????????????????????? ????????????????????? [????????????????????????]


"""
/***********************************************************************************************
 * Run -- Run The Main Program                                                                 *                                                 *
 *                                                                                             *
 *                                                                                             *
 *                                                                                             *
 * INPUT:    Nothing                                                                           *
 *                                                                                             *
 * OUTPUT:   Nothing                                                                           *
 *                                                                                             *
 * WARNINGS: None                                                                              *
 *                                                                                             *
 * HISTORY:                                                                                    *
 *    30/06/22 13:54AM ST : Created                                                            *
 *=============================================================================================*/
"""

if __name__ == '__main__':
    search_path()
