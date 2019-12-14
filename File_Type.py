
import FILE_EXT,FILE_DIR


def f_Type(f_ext):
    if f_ext in FILE_EXT.image_file_tup:
        return(FILE_DIR.image_dir)

    elif f_ext in FILE_EXT.video_file_tup:
        return(FILE_DIR.video_dir)

    elif f_ext in FILE_EXT.audio_file_tup:
        return(FILE_DIR.audio_dir)

    elif f_ext in FILE_EXT.compressed_file_tup:
        return(FILE_DIR.compressed_dir)

    elif f_ext in FILE_EXT.database_file_tup:
        return(FILE_DIR.database_dir)

    elif f_ext in FILE_EXT.torrent_file_tup:
        return(FILE_DIR.torrent_dir)

    elif f_ext in FILE_EXT.executable_file_tup:
        return(FILE_DIR.executable_dir)

    elif f_ext in FILE_EXT.text_file_tup:
        return(FILE_DIR.text_dir)

    elif f_ext in FILE_EXT.system_file_tup:
        return(FILE_DIR.system_dir)

    elif f_ext in FILE_EXT.spreadsheet_file_tup:
        return(FILE_DIR.spreadsheet_dir)

    elif f_ext in FILE_EXT.programming_file_tup:
        return(FILE_DIR.programming_dir)

    elif f_ext in FILE_EXT.presentation_file_tup:
        return(FILE_DIR.presentation_dir)

    elif f_ext in FILE_EXT.net_file_tup:
        return(FILE_DIR.net_dir)

    elif f_ext in FILE_EXT.font_file_tup:
        return(FILE_DIR.font_dir)

    elif f_ext in FILE_EXT.disc_file_tup:
        return(FILE_DIR.disc_dir)

    else:
        return(FILE_DIR.miscellaneous_dir)
