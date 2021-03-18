def getScreenWidthPadded(root, pad):
    if (root.winfo_screenwidth() * pad) > 1920:
        return str(int((root.winfo_screenwidth() * pad) / 2))
    return str(int(root.winfo_screenwidth() * pad))


def getScreenHeightPadded(root, pad):
    if (root.winfo_screenheight() * pad)> 1080:
        return str(int((root.winfo_screenheight() * pad) / 2))
    return str(int(root.winfo_screenheight() * pad))
