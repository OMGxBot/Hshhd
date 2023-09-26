#!/usr/bin/env python3
class WZMLStyle:
    # ----------------------
    # async def start(client, message) ---> __main__.py
    ST_BN1_NAME = 'owner'
    ST_BN1_URL = 'https://t.me/SheikX_TGX'
    ST_BN2_NAME = 'Main Channel'
    ST_BN2_URL = 'https://t.me/SheikX_TGX'
    ST_MSG = '''<i>This bot can mirror all your links|files|torrents to Google Drive or any rclone cloud or to telegram or to ddl servers.</i>
<b>Type {help_command} to get a list of available commands</b>'''
    ST_BOTPM = '''<i>Now, This bot will send all your files and links here. Start Using ...</i>'''
    ST_UNAUTH = '''<i>You Are not authorized user! Deploy your own Mirror-Leech bot</i>'''
    PIC = 'https://graph.org/file/4e04d7306ebc06d5d12e5.jpg'
    # ---------------------

    # async def stats(client, message):
    BOT_STATS = '''⌬ <b><i>BOT STATISTICS :</i></b>
 <b>Bot Uptime :</b> {bot_uptime}

 <b><i>RAM ( MEMORY ) :</i></b>
 {ram_bar} {ram}%
 <b>U :</b> {ram_u} | <b>F :</b> {ram_f} | <b>T :</b> {ram_t}

 <b><i>SWAP MEMORY :</i></b>
 {swap_bar} {swap}%
 <b>U :</b> {swap_u} | <b>F :</b> {swap_f} | <b>T :</b> {swap_t}

 <b><i>DISK :</i></b>
 {disk_bar} {disk}%
 <b>Total Disk Read :</b> {disk_read}
 <b>Total Disk Write :</b> {disk_write}
 <b>U :</b> {disk_u} | <b>F :</b> {disk_f} | <b>T :</b> {disk_t}
    
    '''
    SYS_STATS = ''' <b><i>OS SYSTEM :</i></b>
 <b>OS Uptime :</b> {os_uptime}
 <b>OS Version :</b> {os_version}
 <b>OS Arch :</b> {os_arch}

 <b><i>NETWORK STATS :</i></b>
 <b>Upload Data:</b> {up_data}
 <b>Download Data:</b> {dl_data}
 <b>Pkts Sent:</b> {pkt_sent}k
 <b>Pkts Received:</b> {pkt_recv}k
 <b>Total I/O Data:</b> {tl_data}

 <b>CPU :</b>
 {cpu_bar} {cpu}%
 <b>CPU Frequency :</b> {cpu_freq}
 <b>System Avg Load :</b> {sys_load}
 <b>P-Core(s) :</b> {p_core} | <b>V-Core(s) :</b> {v_core}
 <b>Total Core(s) :</b> {total_core}
 <b>Usable CPU(s) :</b> {cpu_use}
    '''
    REPO_STATS = ''' <b><i>REPO STATISTICS :</i></b>
 <b>Bot Updated :</b> {last_commit}
 <b>Current Version :</b> {bot_version}
 <b>Latest Version :</b> {lat_version}
 <b>Last ChangeLog :</b> {commit_details}

 <b>REMARKS :</b> <code>{remarks}</code>
    '''
    BOT_LIMITS = ''' <b><i>BOT LIMITATIONS :</i></b>
 <b>Direct Limit :</b> {DL} GB
 <b>Torrent Limit :</b> {TL} GB
 <b>GDrive Limit :</b> {GL} GB
 <b>YT-DLP Limit :</b> {YL} GB
 <b>Playlist Limit :</b> {PL}
 <b>Mega Limit :</b> {ML} GB
 <b>Clone Limit :</b> {CL} GB
 <b>Leech Limit :</b> {LL} GB

 <b>Token Validity :</b> {TV}
 <b>User Time Limit :</b> {UTI} / task
 <b>User Parallel Tasks :</b> {UT}
 <b>Bot Parallel Tasks :</b> {BT}
    '''
    # ---------------------

    # async def restart(client, message): ---> __main__.py
    RESTARTING = '<i>Restarting...</i>'
    # ---------------------

    # async def restart_notification(): ---> __main__.py
    RESTART_SUCCESS = '''⌬ <b><i>Restarted Successfully!</i></b>
 <b>Date:</b> {date}
 <b>Time:</b> {time}
 <b>TimeZone:</b> {timz}
 <b>Version:</b> {version}'''
    RESTARTED = '''⌬ <b><i>Bot Restarted!</i></b>'''
    # ---------------------

    # async def ping(client, message): ---> __main__.py
    PING = '<i>Starting Ping..</i>'
    PING_VALUE = '<b>Pong</b>\n<code>{value} ms..</code>'
    # ---------------------

    # async def onDownloadStart(self): --> tasks_listener.py
    LINKS_START = """<b><i>Task Started</i></b>
 <b>Mode:</b> {Mode}
 <b>By:</b> {Tag}\n\n"""
    LINKS_SOURCE = """ <b>Source:</b>
 <b>Added On:</b> {On}
------------------------------------------
{Source}
------------------------------------------\n\n"""
    
    # async def __msg_to_reply(self): ---> pyrogramEngine.py
    PM_START =            "📌 <b><u>ᴛᴀsᴋ sᴛᴀʀᴛᴛᴇᴅ :</u></b>\n\n <b>🔗 ʟɪɴᴋ :</b> <a href='{msg_link}'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>"
    L_LOG_START =           "📌 <b><u>ʟᴇᴇᴄʜ sᴛᴀʀᴛᴛᴇᴅ :</u></b>\n\n<b>🧑‍🎓 ᴜsᴇʀ :</b> {mention} ( #ɪᴅ{uid} )\n<b>🧬 sᴏᴜʀᴄᴇ :</b> <a href='{msg_link}'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>"

    # async def onUploadComplete(): ---> tasks_listener.py
    NAME =                  '<b>📂 ɴᴀᴍᴇ : <code>{Name}</code></b>\n\n'
    SIZE =                  '<b>📦 sɪᴢᴇ : </b><code>{Size}</code>\n'
    ELAPSE =                '<b>🗒️ ᴇʟᴀᴘsᴇᴅ : </b><code>{Time}</code>\n'
    MODE =                  '<b>🕹️ ᴍᴏᴅᴇ : </b><code>{Mode}</code>\n'

    # ----- LEECH -------
    L_TOTAL_FILES =         '<b>🗃️ ᴛᴏᴛᴀʟ ғɪʟᴇs : </b><code>{Files}</code>\n'
    L_CORRUPTED_FILES =     '<b>📑 ᴄᴏʀʀᴜᴘᴛᴇᴅ ғɪʟᴇs : </b><code>{Corrupt}</code>\n'
    L_CC =                  '<b>🎭 ᴜᴘʟᴏᴅᴇ ʙʏ: </b>{Tag}</code>\n\n'
    PM_BOT_MSG =            '<b>🔰 ғɪʟᴇ ʜᴀᴠᴇ ʙᴇᴇɴ sᴇɴᴛ ᴀʙᴏᴠᴇ\n\n~ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ ›› <a href="https://t.me/Hari_OP">ʜᴀʀɪ ᠰ ᴛɢ​</a></b>'
    L_BOT_MSG =             '<b>🔰 ғɪʟᴇ (ꜱ) ʜᴀᴠᴇ ʙᴇᴇɴ sᴇɴᴛ ᴛᴏ ʙᴏᴛ ᴘᴍ ᴘʀɪᴠᴀᴛᴇ\n\n~ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ ›› <a href="https://t.me/Hari_OP">ʜᴀʀɪ ᠰ ᴛɢ​</a></b>'
    L_LL_MSG =              '<b>🔰 ғɪʟᴇ (ꜱ) ʜᴀᴠᴇ ʙᴇᴇɴ sᴇɴᴛ. ᴀᴄᴄᴇꜱꜱ ᴠɪᴀ ʟɪɴᴋꜱ...\n\n~ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ ›› <a href="https://t.me/Hari_OP">ʜᴀʀɪ ᠰ ᴛɢ</a></b>'
    
    # ----- MIRROR -------
    M_TYPE =                '<b>🗒️ ᴛʏᴘᴇ : </b><code>{Mimetype}</code>\n'
    M_SUBFOLD =             '<b>🗃️ sᴜʙғᴏʟᴅᴇʀs : </b><code>{Folder}</code>\n'
    TOTAL_FILES =           '<b>🗂️ ғɪʟᴇs : </b><code>{Files}</code>\n'
    RCPATH =                '<b>🗞️ ᴘᴀᴛʜ : </b><code>{RCpath}</code>\n'
    M_CC =                  '<b>🎭 ᴜᴘʟᴏᴅᴇ : </b>{Tag}\n\n'
    M_BOT_MSG =             '<b>🔰 ʟɪɴᴋ (ꜱ) ʜᴀᴠᴇ ʙᴇᴇɴ sᴇɴᴛ ᴛᴏ ʙᴏᴛ ᴘᴍ ᴘʀɪᴠᴀᴛᴇ</b>'
    
    # ----- BUTTONS -------
    CLOUD_LINK =      '☁️ ᴄʟᴏᴜᴅ ʟɪɴᴋ'
    SAVE_MSG =        '📨 sᴀᴠᴇ ᴍᴇᴇssᴀɢᴇ'
    RCLONE_LINK =     '♻️ ʀᴄʟᴏɴᴇ ʟɪɴᴋ'
    DDL_LINK =        '📎 {Serv} ʟɪɴᴋ'
    SOURCE_URL =      '🔐 sᴏᴜʀᴄᴇ ʟɪɴᴋ'
    INDEX_LINK_F =    '🗂 ɪɴᴅᴇx ʟɪɴᴋ'
    INDEX_LINK_D =    '⚡ ɪɴᴅᴇx ʟɪɴᴋ'
    VIEW_LINK =       '🌐 ᴠɪᴇᴡ ʟɪɴᴋ'
    CHECK_PM =        '🗳️ ᴠɪᴇᴡ ɪɴ ʙᴏᴛ ᴘᴍ'
    CHECK_LL =        '🖇 ᴠɪᴇᴡ ɪɴ ʟɪɴᴋ ʟᴏɢ'
    MEDIAINFO_LINK =  '📃 ᴍᴇᴅɪᴀ ɪɴғᴏ'
    # ---------------------

    # def get_readable_message(): ---> bot_utilis.py
    ####--------OVERALL MSG HEADER----------
    STATUS_NAME =       '<b>✓ ғɪʟᴇ ɴᴀᴍᴇ</b> : <code>{Name}</code>\n'

    #####---------PROGRESSIVE STATUS-------
    BAR =               '\n<b>» <a href="https://t.me/Hari_OP">{Bar}</a></b>'
    PROCESSED =         '\n<b>» ᴘʀᴏᴄᴇssᴇᴅ :</b> <code>{Processed}</code>'
    STATUS =            '\n<b>» sᴛᴀᴛᴜs :</b> <b><a href="{Url}">{Status}</a></b>'
    ETA =                                                ' | <b>ᴇᴛᴀ :</b> <code>{Eta}</code>'
    SPEED =             '\n<b>» sᴘᴇᴇᴅ :</b> <code>{Speed}</code>'
    ELAPSED =                                     ' | <b>ᴇʟᴀᴘsᴇᴅ :</b> <code>{Elapsed}</code>'
    ENGINE =            '\n<b>» ᴇɴɢɪɴᴇ :</b> <code>{Engine}</code>'
    STA_MODE =          '\n<b>» ᴍᴏᴅᴇ :</b> <code>{Mode}</code>'
    SEEDERS =           '\n<b>» sᴇᴇᴅᴇʀs :</b> <code>{Seeders}</code> | '
    LEECHERS =                                           '<b>ʟᴇᴇᴄʜᴇʀs :</b> <code>{Leechers}</code>'
    
    ####--------SEEDING----------
    SEED_SIZE =      '\n<b>» sɪᴢᴇ : </b><code> {Size}</code>'
    SEED_SPEED =     '\n<b>» sᴘᴇᴇᴅ : </b> <code>{Speed}</code> | '
    UPLOADED =                                     '<b>ᴜᴘʟᴏᴀᴅᴇᴅ :</b> <code>{Upload}</code>'
    RATIO =          '\n<b>» ʀᴀᴛɪᴏ : </b> <code>{Ratio}</code> | '
    TIME =                                         '<b>ᴛɪᴍᴇ : </b> <code>{Time}</code>'
    SEED_ENGINE =    '\n<b>» ᴇɴɢɪɴᴇ :</b> <code>{Engine}</code>'

    ####--------NON-PROGRESSIVE + NON SEEDING----------
    STATUS_SIZE =    '\n<b>» sɪᴢᴇ : </b><code> {Size}</code>'
    NON_ENGINE =     '\n<b>» ᴇɴɢɪɴᴇ :</b> <code>{Engine}</code>'

    ####--------OVERALL MSG FOOTER----------
    USER =              '\n<b>» ᴜsᴇʀ :</b> <code>{User}</code> | '
    ID =                                                        '<b>ɪᴅ :</b> <code>{Id}</code>'
    BTSEL =          '\n<b>» sᴇʟᴇᴄᴛ :</b> <code>{Btsel}</code>'
    CANCEL =         '\n<b>» ᴄᴀɴᴄᴇʟ :</b> <code>{Cancel}</code>\n\n'
    
    ####------FOOTER--------
    FOOTER = '<u><b>ʙᴏᴛ sᴛᴀᴛs</b></u>\n\n'
    TASKS =  '<b>» ᴛᴀsᴋs :</b> <code>{Tasks}</code>\n'
    BOT_TASKS = '<b>» ᴛᴀsᴋs :</b> <code>{Tasks}/{Ttask}</code> | <b>ᴀᴠʟ :</b> <code>{Free}</code>\n'
    Cpu = '<b>» ᴄᴘᴜ :</b> <code>{cpu}%</code> | '
    FREE =                      '<b>ғʀᴇᴇ :</b> <code>{free} [{free_p}%]</code>'
    Ram = '\n<b>» ʀᴀᴍ :</b> <code>{ram}%</code> | '
    uptime =                     '<b>ᴜᴘᴛɪᴍᴇ :</b> <code>{uptime}</code>'
    DL = '\n<b>» ᴅʟ :</b> <code>{DL}/s</code> | '
    UL =                        '<b>ᴜʟ :</b> <code>{UL}/s</code>'

    ###--------BUTTONS-------
    PREVIOUS = '⇇ ʙᴀᴄᴋ'
    REFRESH = 'ᴘᴀɢᴇs\n{Page}'
    NEXT = 'ɴᴇxᴛ ⇉'
    # ---------------------

    #STOP_DUPLICATE_MSG: ---> clone.py, aria2_listener.py, task_manager.py
    STOP_DUPLICATE = 'File/Folder is already available in Drive.\nHere are {content} list results:'
    # ---------------------

    # async def countNode(_, message): ----> gd_count.py
    COUNT_MSG = '<b>Counting:</b> <code>{LINK}</code>'
    COUNT_NAME = '<b><i>{COUNT_NAME}</i></b>\n\n'
    COUNT_SIZE = ' <b>Size: </b>{COUNT_SIZE}\n'
    COUNT_TYPE = ' <b>Type: </b>{COUNT_TYPE}\n'
    COUNT_SUB =  ' <b>SubFolders: </b>{COUNT_SUB}\n'
    COUNT_FILE = ' <b>Files: </b>{COUNT_FILE}\n'
    COUNT_CC =   ' <b>By: </b>{COUNT_CC}\n'
    # ---------------------

    # LIST ---> gd_list.py
    LIST_SEARCHING = '<b>Searching for <i>{NAME}</i></b>'
    LIST_FOUND = '<b>Found {NO} result for <i>{NAME}</i></b>'
    LIST_NOT_FOUND = 'No result found for <i>{NAME}</i>'
    # ---------------------

    # async def mirror_status(_, message): ----> status.py
    NO_ACTIVE_DL = '''<b>ɴᴏ ᴀᴄᴛɪᴠᴇ ᴅᴏᴡɴʟᴏᴀᴅs !</b>
    
🧵 <b>ʙᴏᴛ sᴛᴀᴛs</b> 🧵

<b>ᴄᴘᴜ :</b> <code>{cpu}%</code> | <b>ғʀᴇʀ :</b> <code>{free} [{free_p}%]</code>
<b>ʀᴀᴍ :</b> <code>{ram}</code> | <b>ᴜᴘᴛɪᴍᴇ :</b> <code>{uptime}</code>
    '''
    # ---------------------

    # USER Setting --> user_setting.py 
    USER_SETTING = '''🎭 <b>ᴜsᴇʀ sᴇᴛᴛɪɴɢs :</b>
        
<b>~ ɴᴀᴍᴇ :</b> {NAME} ( <code>{ID}</code> )
<b>~ ᴜsᴇʀ ɴᴀᴍᴇ :</b> {USERNAME}
<b>~ ᴛᴇʟᴇɢʀᴀɴ ᴅᴄ :</b> {DC}
<b>~ ʟᴀɴɢᴜᴀɢᴇ :</b> {LANG}

<b>~ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ ›› <a href='https://t.me/Hari_OP'>ʜᴀʀɪ ᠰ ᴛɢ​</a></b>'''
    
    UNIVERSAL = '''🍂 <b><u>ᴜɴɪᴠᴇʀsᴀʟ sᴇᴛᴛɪɴɢs : {NAME}</u></b>

<b>~ ʏᴛ-ᴅʟᴘ ᴏᴘᴛɪᴏɴs :</b> <b><code>{YT}</code></b>
<b>~ ᴅᴀɪʟʏ ᴛᴀsᴋs :</b> <code>{DT}</code> per day
<b>~ ʟᴀsᴛ ʙᴏᴛ ᴜsᴇᴅ :</b> <code>{LAST_USED}</code>
<b>~ ᴍᴇᴅɪᴀ ɪɴғᴏ ᴍᴏᴅᴇ :</b> <code>{MEDIAINFO}</code>
<b>~ sᴀᴠᴇ ᴍᴏᴅᴇ :</b> <code>{SAVE_MODE}</code>
<b>~ ᴜsᴇʀ ʙᴏᴛ ᴘᴍ :</b> <code>{BOT_PM}</code>

<b>~ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ ›› <a href='https://t.me/Hari_OP'>ʜᴀʀɪ ᠰ ᴛɢ​</a></b>'''

    MIRROR = '''🖌️ <b><u>ᴍɪʀʀᴏʀ-ᴄʟᴏɴᴇ sᴇᴛᴛɪɴɢs : {NAME}</u></b>

<b>~ ʀᴄʟᴏɴᴇ ᴄᴏɴғɪɢ :</b> <i>{RCLONE}</i>
<b>~ ᴍɪʀʀᴏʀ ᴘʀᴇғɪx :</b> <code>{MPREFIX}</code>
<b>~ ᴍɪʀʀᴏʀ sᴜғғɪx :</b> <code>{MSUFFIX}</code>
<b>~ ᴍɪʀʀᴏʀ ʀᴇᴍɴᴀᴍᴇ :</b> <code>{MREMNAME}</code>
<b>~ ᴅᴅʟ sᴇʀᴠᴇʀ(s):</b> <i>{DDL_SERVER}</i>
<b>~ ᴜsᴇʀ ᴛᴅ ᴍᴏᴅᴇ :</b> <i>{TMODE}</i>
<b>~ ᴛᴏᴛᴀʟ ᴜsᴇʀ ᴛᴅ(s) :</b> <i>{USERTD}</i>
<b>~ ᴅᴀɪʟʏ ᴍɪʀʀᴏʀ :</b> <code>{DM}</code> per day

<b>~ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ ›› <a href='https://t.me/Hari_OP'>ʜᴀʀɪ ᠰ ᴛɢ​</a></b>'''
    
    LEECH = '''🥀 <b><u>ʟᴇᴇᴄʜ sᴇᴛᴛɪɴɢs ғᴏʀ - {NAME}</u></b>

<b>~ ᴅᴀɪʟʏ ʟᴇᴇᴄʜ : </b><code>{DL}</code> per day
<b>~ ʟᴇᴇᴄʜ ᴛʏᴘᴇ :</b> <i>{LTYPE}</i>
<b>~ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ :</b> <i>{THUMB}</i>
<b>~ ʟᴇᴇᴄʜ sᴘʟɪᴛ sɪᴢᴇ :</b> <code>{SPLIT_SIZE}</code>
<b>~ ᴇǫᴜᴀʟ sᴘʟɪᴛs :</b> <i>{EQUAL_SPLIT}</i>
<b>~ ᴍᴇᴅɪᴀ ɢʀᴏᴜᴘ :</b> <i>{MEDIA_GROUP}</i>
<b>~ ʟᴇᴇᴄʜ ᴄᴀᴘᴛɪᴏɴ :</b> <code>{LCAPTION}</code>
<b>~ ʟᴇᴇᴄʜ ᴘʀᴇғɪx :</b> <code>{LPREFIX}</code>
<b>~ ʟᴇᴇᴄʜ sᴜғғɪx :</b> <code>{LSUFFIX}</code>
<b>~ Leech ᴅᴜᴍᴘs :</b> <code>{LDUMP}</code>
<b>~ ʟᴇᴇᴄʜ ʀᴇᴍᴀɴᴍᴇ :</b> <code>{LREMNAME}</code>

<b>~ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ ›› <a href='https://t.me/Hari_OP'>ʜᴀʀɪ ᠰ ᴛɢ​</a></b>'''
