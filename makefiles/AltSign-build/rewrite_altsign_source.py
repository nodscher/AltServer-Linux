#!/usr/bin/python3

import re
import sys

F = sys.argv[1]

with open(F, 'rb') as f:
    content = f.read()

content = re.sub(br'L("([^"\\]|\\.)*")', br'U(\1)', content)
content = content.replace(b'std::wstring', b'std::string')
content = content.replace(b'boost/filesystem.hpp', b'filesystem')
content = content.replace(b'boost::filesystem', b'std::filesystem')

content = content.replace(b'"%FT%T%z"', b'"%Y-%m-%dT%H:%M:%SZ"')
content = content.replace(b'localtime(', b'gmtime(')

content = content.replace(b'winsock2.h', b'WinSock2.h')

content = re.sub(br'plist_from_memory\s*\((.*)\)', br'plist_from_memory(\1, NULL)', content)


# Always insert #include <vector> after #include <fstream> in Archiver.cpp
if F.endswith("Archiver.cpp"):
    content = content.replace(
        b'#include <fstream>',
        b'#include <fstream>\n#include <vector>'
    )

sys.stdout.buffer.write(content)