import bot
import tc_pc_scan
import multiprocessing
import time


def startBot():
    print("Bot starting...")
    bot.bot.run(bot.TOKEN)


def startCheckRoom():
    while True:
        print("Check in progress...")
        tc_pc_scan.save_pickle(tc_pc_scan.scan_rooms(list(tc_pc_scan.ROOMS)), "rooms.pkl")
        print("All rooms was scanned, next scan in 600 secs")
        time.sleep(600)


if __name__ == '__main__':
    BotProcess = multiprocessing.Process(target=startBot)
    ScanProcess = multiprocessing.Process(target=startCheckRoom)

    process = [BotProcess, ScanProcess, ]

    for p in process:
        p.start()

    for p in process:
        p.join()
