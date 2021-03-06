"""
this module define some constances and structs
import some win32API
by 原照萌
"""

from ctypes import *

# import win32API
SetWindowsHookEx = windll.user32.SetWindowsHookExA
GetCurrentThreadId = windll.kernel32.GetCurrentThreadId
GetModuleHandle = windll.kernel32.GetModuleHandleA
GetMessage = windll.user32.GetMessageA
TranslateMessage = windll.user32.TranslateMessage
DispatchMessage = windll.user32.DispatchMessageA
UnhookWindowsHookEx = windll.user32.UnhookWindowsHookEx
PostThreadMessage = windll.user32.PostThreadMessageA
CallNextHookEx = windll.user32.CallNextHookEx
RegisterHotKey = windll.user32.RegisterHotKey
UnregisterHotKey = windll.user32.UnregisterHotKey

keybd_event = windll.user32.keybd_event
mouse_event = windll.user32.mouse_event
SetCursorPos = windll.user32.SetCursorPos
GetCursorPos = windll.user32.GetCursorPos


# virtual Key code
VK_list = {
    "VK_LBUTTON": 0x01,
    "VK_RBUTTON": 0x02,
    "VK_CANCEL": 0x03,
    "VK_MBUTTON": 0x04,
    "VK_XBUTTON1": 0x05,
    "VK_XBUTTON2": 0x06,
    "VK_BACK": 0x08,
    "VK_TAB": 0x09,
    "VK_CLEAR": 0x0C,
    "VK_RETURN": 0x0D,
    "VK_SHIFT": 0x10,
    "VK_CONTROL": 0x11,
    "VK_MENU": 0x12,
    "VK_PAUSE": 0x13,
    "VK_CAPITAL": 0x14,
    "VK_KANA": 0x15,
    "VK_HANGEUL": 0x15,
    "VK_HANGUL": 0x15,
    "VK_JUNJA": 0x17,
    "VK_FINAL": 0x18,
    "VK_HANJA": 0x19,
    "VK_KANJI": 0x19,
    "VK_ESCAPE": 0x1B,
    "VK_CONVERT": 0x1C,
    "VK_NONCONVERT": 0x1D,
    "VK_ACCEPT": 0x1E,
    "VK_MODECHANGE": 0x1F,
    "VK_SPACE": 0x20,
    "VK_PRIOR": 0x21,
    "VK_NEXT": 0x22,
    "VK_END": 0x23,
    "VK_HOME": 0x24,
    "VK_LEFT": 0x25,
    "VK_UP": 0x26,
    "VK_RIGHT": 0x27,
    "VK_DOWN": 0x28,
    "VK_SELECT": 0x29,
    "VK_PRINT": 0x2A,
    "VK_EXECUTE": 0x2B,
    "VK_SNAPSHOT": 0x2C,
    "VK_INSERT": 0x2D,
    "VK_DELETE": 0x2E,
    "VK_HELP": 0x2F,
    # 0-9、A-Z 可直接通过ord()来获得
    "0": 0x30,
    "1": 0x31,
    "2": 0x32,
    "3": 0x33,
    "4": 0x34,
    "5": 0x35,
    "6": 0x36,
    "7": 0x37,
    "8": 0x38,
    "9": 0x39,
    # 0x3A-0x4F 保留
    "A": 0x41,
    "B": 0x42,
    "C": 0x43,
    "D": 0x44,
    "E": 0x45,
    "F": 0x46,
    "G": 0x47,
    "H": 0x48,
    "I": 0x49,
    "J": 0x4A,
    "K": 0x4B,
    "L": 0x4C,
    "M": 0x4D,
    "N": 0x4E,
    "O": 0x4F,
    "P": 0x50,
    "Q": 0x51,
    "R": 0x52,
    "S": 0x53,
    "T": 0x54,
    "U": 0x55,
    "V": 0x56,
    "W": 0x57,
    "X": 0x58,
    "Y": 0x59,
    "Z": 0x5A,
    "VK_LWIN": 0x5B,
    "VK_RWIN": 0x5C,
    "VK_APPS": 0x5D,
    "VK_SLEEP": 0x5F,
    "VK_NUMPAD0": 0x60,
    "VK_NUMPAD1": 0x61,
    "VK_NUMPAD2": 0x62,
    "VK_NUMPAD3": 0x63,
    "VK_NUMPAD4": 0x64,
    "VK_NUMPAD5": 0x65,
    "VK_NUMPAD6": 0x66,
    "VK_NUMPAD7": 0x67,
    "VK_NUMPAD8": 0x68,
    "VK_NUMPAD9": 0x69,
    "VK_MULTIPLY": 0x6A,
    "VK_ADD": 0x6B,
    "VK_SEPARATOR": 0x6C,
    "VK_SUBTRACT": 0x6D,
    "VK_DECIMAL": 0x6E,
    "VK_DIVIDE": 0x6F,
    "VK_F1": 0x70,
    "VK_F2": 0x71,
    "VK_F3": 0x72,
    "VK_F4": 0x73,
    "VK_F5": 0x74,
    "VK_F6": 0x75,
    "VK_F7": 0x76,
    "VK_F8": 0x77,
    "VK_F9": 0x78,
    "VK_F10": 0x79,
    "VK_F11": 0x7A,
    "VK_F12": 0x7B,
    "VK_F13": 0x7C,
    "VK_F14": 0x7D,
    "VK_F15": 0x7E,
    "VK_F16": 0x7F,
    "VK_F17": 0x80,
    "VK_F18": 0x81,
    "VK_F19": 0x82,
    "VK_F20": 0x83,
    "VK_F21": 0x84,
    "VK_F22": 0x85,
    "VK_F23": 0x86,
    "VK_F24": 0x87,
    "VK_NUMLOCK": 0x90,
    "VK_SCROLL": 0x91,
    "VK_OEM_NEC_EQUAL": 0x92,
    "VK_OEM_FJ_JISHO": 0x92,
    "VK_OEM_FJ_MASSHOU": 0x93,
    "VK_OEM_FJ_TOUROKU": 0x94,
    "VK_OEM_FJ_LOYA": 0x95,
    "VK_OEM_FJ_ROYA": 0x96,
    "VK_LSHIFT": 0xA0,
    "VK_RSHIFT": 0xA1,
    "VK_LCONTROL": 0xA2,
    "VK_RCONTROL": 0xA3,
    "VK_LMENU": 0xA4,
    "VK_RMENU": 0xA5,
    "VK_BROWSER_BACK": 0xA6,
    "VK_BROWSER_FORWARD": 0xA7,
    "VK_BROWSER_REFRESH": 0xA8,
    "VK_BROWSER_STOP": 0xA9,
    "VK_BROWSER_SEARCH": 0xAA,
    "VK_BROWSER_FAVORITES": 0xAB,
    "VK_BROWSER_HOME": 0xAC,
    "VK_VOLUME_MUTE": 0xAD,
    "VK_VOLUME_DOWN": 0xAE,
    "VK_VOLUME_UP": 0xAF,
    "VK_MEDIA_NEXT_TRACK": 0xB0,
    "VK_MEDIA_PREV_TRACK": 0xB1,
    "VK_MEDIA_STOP": 0xB2,
    "VK_MEDIA_PLAY_PAUSE": 0xB3,
    "VK_LAUNCH_MAIL": 0xB4,
    "VK_LAUNCH_MEDIA_SELECT": 0xB5,
    "VK_LAUNCH_APP1": 0xB6,
    "VK_LAUNCH_APP2": 0xB7,
    "VK_OEM_1": 0xBA,
    "VK_OEM_PLUS": 0xBB,
    "VK_OEM_COMMA": 0xBC,
    "VK_OEM_MINUS": 0xBD,
    "VK_OEM_PERIOD": 0xBE,
    "VK_OEM_2": 0xBF,
    "VK_OEM_3": 0xC0,
    "VK_OEM_4": 0xDB,
    "VK_OEM_5": 0xDC,
    "VK_OEM_6": 0xDD,
    "VK_OEM_7": 0xDE,
    "VK_OEM_8": 0xDF,
    "VK_OEM_AX": 0xE1,
    "VK_OEM_102": 0xE2,
    "VK_ICO_HELP": 0xE3,
    "VK_ICO_00": 0xE4,
    "VK_PROCESSKEY": 0xE5,
    "VK_ICO_CLEAR": 0xE6,
    "VK_PACKET": 0xE7,
    "VK_OEM_RESET": 0xE9,
    "VK_OEM_JUMP": 0xEA,
    "VK_OEM_PA1": 0xEB,
    "VK_OEM_PA2": 0xEC,
    "VK_OEM_PA3": 0xED,
    "VK_OEM_WSCTRL": 0xEE,
    "VK_OEM_CUSEL": 0xEF,
    "VK_OEM_ATTN": 0xF0,
    "VK_OEM_FINISH": 0xF1,
    "VK_OEM_COPY": 0xF2,
    "VK_OEM_AUTO": 0xF3,
    "VK_OEM_ENLW": 0xF4,
    "VK_OEM_BACKTAB": 0xF5,
    "VK_ATTN": 0xF6,
    "VK_CRSEL": 0xF7,
    "VK_EXSEL": 0xF8,
    "VK_EREOF": 0xF9,
    "VK_PLAY": 0xFA,
    "VK_ZOOM": 0xFB,
    "VK_NONAME": 0xFC,
    "VK_PA1": 0xFD,
    "VK_OEM_CLEAR": 0xFE}

# mouse event,for sending mouse keys
# https://msdn.microsoft.com/en-us/library/windows/desktop/ms646260(v=vs.85).aspx
ME_list = {
    'LD': 0x0002,  # mouse left button down
    'LU': 0x0004,  # mouse left button up
    'LP': 0x2 | 0x4,  # mouse left press
    'MD': 0x0020,  # middle button
    'MU': 0x0040,
    'MP': 0x20 | 0x40,
    'RD': 0x0008,  # right button
    'RU': 0x0010,
    'RP': 0x8 | 0x10,
    'WHEEL': 0x0800  # the wheel move,The amount of movement is specified in dwData
}

# wParam in LowLevelMouseProc
# https://msdn.microsoft.com/en-us/library/ms644986(v=vs.85).aspx
VM_list = {
    'LD': 0x0201,  # left button down
    'LU': 0x0202,  # left button up
    'RD': 0x0204,  # right button down
    'RU': 0x0205,  # right button up
    'MM': 0x0200,  # MouseMove event
    'MW': 0x020A,  # MouseWheel
    'MHW': 0x020E  # mouse horizontal wheel
}

MOD_list = {'alt': 0x0001,
            'ctrl': 0x0002,
            'shift': 0x0004,
            'win': 0x0008}


class VK:
    def __getattr__(self, item):
        return VK_list[item]


class VM:
    def __getattr__(self, item):
        return VM_list[item]


class ME:
    def __getattr__(self, item):
        return ME_list[item]


class MOD:
    def __getattr__(self, item):
        return MOD_list[item]


vk = VK()
vk.__doc__ = "键盘虚拟按键的代码，想获得全部可用的列表，请使用VK_list,它是一个字典。"
vm = VM()
vm.__doc__ = "监视鼠标时接受的代码，不用于发送按键。"
mod = MOD()
mod.__doc__ = "辅助按键的代码,用于设置热键。"
me = ME()
me.__doc__ = "鼠标的虚拟按键代码，详见 VM_list,发送按键时用的参数，不用于监控按键"

# 消息循环的常量，也就是mainloop中的msg.message
WM_QUIT = 0x12
WM_HOTKEY = 0x0312
WM_USER = 0x400


class POINT(Structure):
    _fields_ = [('x', c_int),
                ('y', c_int)]


# make some struct for functions
'''
typedef struct tagMSG {
  HWND   hwnd;
  UINT   message;
  WPARAM wParam;
  LPARAM lParam;
  DWORD  time;
  POINT  pt;
} MSG, *PMSG, *LPMSG;
'''


class MSG(Structure):
    _fields_ = [('hwnd', c_void_p),
                ('message', c_uint),
                ('wParam', c_uint),
                ('lParam', c_uint),
                ('time', c_uint),
                ('pt', c_void_p)]


'''
typedef struct tagKBDLLHOOKSTRUCT {
  DWORD     vkCode;
  DWORD     scanCode;
  DWORD     flags;
  DWORD     time;
  ULONG_PTR dwExtraInfo;
} KBDLLHOOKSTRUCT, *PKBDLLHOOKSTRUCT, *LPKBDLLHOOKSTRUCT;
'''


class KBDLLHOOKSTRUCT(Structure):
    _fields_ = [('vkCode', c_int),
                ('scanCode', c_int),
                ('flags', c_int),
                ('time', c_int),
                ('dwExtraInfo', c_void_p)]


'''
typedef struct tagMSLLHOOKSTRUCT {
  POINT     pt;
  DWORD     mouseData;
  DWORD     flags;
  DWORD     time;
  ULONG_PTR dwExtraInfo;
} MSLLHOOKSTRUCT, *PMSLLHOOKSTRUCT, *LPMSLLHOOKSTRUCT;
'''


class MSLLHOOKSTRUCT(Structure):
    _fields_ = [('pt', POINT),
                ('mouseData', c_int),
                ('flags', c_int),
                ('time', c_int),
                ('dwExtrInfo', c_void_p)]


# 这个列表应该用元组来设置每一个消息的常量数字，以及对应的回调函数。
# 如 [(130,Unhookkeyboard),(131,Unhookmouse)]
msg_list = {}


# it record the threadid ,when you post message to the loop ,you need it
threadId = 0


def closeloop():
    global threadId
    if threadId != 0:
        PostThreadMessage(threadId, WM_QUIT, 0, 0)  # Post WM_QUIT message to mainloop
        threadId = 0


def mainloop():
    global threadId
    threadId = GetCurrentThreadId()
    msg = MSG()
    while GetMessage(byref(msg), c_void_p(None), 0, 0) > 0:
        for msgnum, func in msg_list.items():
            if msg.message == msgnum:
                func()

        TranslateMessage(byref(msg))
        DispatchMessage(byref(msg))






