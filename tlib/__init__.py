from sys import stdin
from os import path
from requests import get
from tqdm import tqdm
from subprocess import run
import re

def download(url: str, fname: str):
    try:
        with open(fname, "ab") as f, tqdm(
        ) as bar:
            headers = {}
            pos = f.tell()
            if pos:
                headers["Range"] = f"bytes={pos}-"
            resp = get(url, headers=headers, stream=True)
            total_size = int(resp.headers.get("content-length", 0))
            bar.desc=fname
            bar.iterable=resp.iter_content(chunk_size=1024)
            bar.total=total_size
            bar.unit="iB"
            bar.unit_scale=True
            bar.unit_divisor=1024
            for data in resp.iter_content(chunk_size=1024):
                size = f.write(data)
                bar.update(size)
    except KeyboardInterrupt:
        quit()

def gen(num, sep):
    i, o = 0, ""
    while i < num:
        o += sep
        i += 1
    return o


def ezstdin():
    if stdin.isatty():
        o = False
        return o
    else:
        o = []
        for line in stdin.readlines():
            o.append(line)
        return o


def arch(line):
    e = "------------------------------------------\n|                   -`                   |\n|                  .o+`                  |\n|                 `ooo/                  |\n|                `+oooo:                 |\n|               `+oooooo:                |\n|               -+oooooo+:               |\n|             `/:-:++oooo+:              |\n|            `/++++/+++++++:             |\n|           `/++++++++++++++:            |\n|          `/+++ooooooooooooo/`          |\n|         ./ooosssso++osssssso+`         |\n|        .oossssso-````/ossssss+`        |\n|       -osssssso.      :ssssssso.       |\n|      :osssssss/        osssso+++.      |\n|     /ossssssss/        +ssssooo/-      |\n|   `/ossssso+/:-        -:/+osssso+-    |\n|  `+sso+:-`                 `.-/+oso:   |\n| `++:.                           `-/+/  |\n| .`                                 `/  |\n------------------------------------------"
    e1 = e.replace("-", "").replace("|", "")[1:]
    if line == True:
        return e
    if line == False:
        return e1


def clean(str): return str.lstrip().rstrip().strip()


def hrs(size, decimal_places=3) -> bool:
    """
    Converts a file's size in bytes to a more human readable format.
    for unit in ['B','KiB','MiB','GiB','TiB']:
        if size < 1024.0:
            break
        size /= 1024.0
    return f"{size:.{decimal_places}f} {unit}"
    """
    for unit in ['B', 'KiB', 'MiB', 'GiB', 'TiB']:
        if size < 1024.0:
            break
        size /= 1024.0
    return f"{size:.{decimal_places}f} {unit}"


def r(cmd): return run(cmd, shell=True,
                       capture_output=True, text=True).stdout.rstrip()


def isVideo(_file: str) -> bool:
    """
    Returns True if the file's extension matches any common video format, returns False otherwise.
    :param _file:
    :type _file: str
    :returns: A bool
    :rtype: bool
    """
    if path.splitext(_file)[-1] in ['.m4v', '.mp4', '.mov', '.wmv', '.avi', '.mpg', '.mpeg', '.rmvb', '.rm', '.flv', '.asf', '.mkv', '.webm']:
        return True
    else:
        return False


def isImage(_file: str) -> bool:
    """
    Returns True if the file's extension matches any common image format, returns False otherwise.
    :param _file:
    :type _file: str
    :returns: A bool
    :rtype: bool
    """
    if path.splitext(_file)[-1] in ['.png', '.jpg', '.jpeg', '.gif', '.webp']:
        return True
    else:
        return False


def isAudio(_file: str) -> bool:
    """
    Returns True if the file's extension matches any common audio format, returns False otherwise.
    :param _file:
    :type _file: str
    :returns: A bool
    :rtype: bool
    """
    if path.splitext(_file)[-1] in ['.mp3', '.aac', '.ogg', '.m4a', '.wma', '.flac', '.wav']:
        return True
    else:
        return False


def isDir(_directory: str) -> bool:
    """
    Checks if _directory is an actual directory and returns a corresponding bool.
    :param _directory: Path the the directory.
    :type _directory: str
    :returns: A boolean that is True if _directory is a directory, returns False if it doesn't exist and/or it's not a directory.
    :rtype: bool
    """
    try:
        _dir = open(_directory, 'r')
        _dir.close()
    except IsADirectoryError:
        return True
    except FileNotFoundError:
        return False
    return False


def parseCookieFile(cookiefile: str) -> dict:
    """Parse a cookies.txt file and return a dictionary of key value pairs
    compatible with requests."""

    cookies: dict = {}
    with open(cookiefile, 'r') as fp:
        for line in fp:
            if not re.match(r'^\#', line) and line not in ['\n']:
                lineFields = line.strip().split('\t')
                cookies[lineFields[-1 - 1]] = lineFields[-1]
    return cookies
