import asyncio
import random

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)

BOT_TOKEN = "8275768269:AAGIzQjtUIhIUTZCkMmNadSagJsAjTnkRIg"

# Store running tasks
spam_tasks = {}

# 30+ random uploader messages
MESSAGES = [
    "Uploading...",
    "Upload Started",
    "Season 1",
    "Episode 1",
    "Part 01",
    "Almost Done...",
    "Uploading Episode...",
    "New Episode Coming...",
    "Stay Tuned...",
    "Release Soon...",
    "HD Print Uploading...",
    "720p Uploading....",
    "Done ✅",
    "Completed 🎉"
    "📤 Uploading Episode... Please wait while we process high quality content for you.",
    "⚡ Upload in progress... Encoding video into multiple resolutions (480p / 720p / 1080p).",
    "🎬 Episode release ongoing... Stay tuned, links will be available shortly.",
    "🔥 New episode is being uploaded... Preparing files for smooth streaming experience.",
    "📦 Packing episode files... Compressing and optimizing for faster downloads.",
    "🚀 Upload started successfully... Sit back and enjoy, content is on the way.",
    "🎥 Processing video... Adjusting bitrate and quality for best output.",
    "🌀 Upload queue active... Your requested anime is currently being uploaded.",
    "📡 Server syncing files... Episode will be live in a few minutes.",
    "💫 Finalizing upload... Almost ready to share with you all.",
    "🔄 Encoding in progress... Please wait while we prepare HD version.",
    "📀 Converting video format... Ensuring compatibility across devices.",
    "🎯 Preparing episode release... Stay connected for instant updates.",
    "📁 Uploading batch files... Multiple parts will be available soon.",
    "🕒 Upload in progress... Estimated time remaining: few minutes.",
    "🌐 Distributing files across servers... Faster access guaranteed.",
    "🎉 Episode almost ready... Finishing touches in progress.",
    "📤 Uploading Part 1... Remaining parts will follow shortly.",
    "📤 Uploading Part 2... Stay tuned for next segments.",
    "📤 Uploading Part 3... Final part coming soon.",
    "🔗 Generating download links... Please wait...",
    "📥 Preparing download options... Multiple qualities incoming.",
    "⚙️ Processing request... Your anime episode is being handled.",
    "📺 Rendering episode preview... High quality ensured.",
    "🧩 Splitting large files... Uploading in smaller parts.",
    "💻 Server load high... Upload may take slightly longer than usual.",
    "🚧 Upload under progress... Do not leave, content arriving soon.",
    "📊 Checking file integrity... Ensuring no corruption.",
    "🎞️ Preparing subtitles... Syncing with video timeline.",
    "🌟 High quality encode in progress... Worth the wait!",
    "📡 Upload pipeline active... Files moving to public servers.",
    "🔒 Securing files... Upload will be available shortly.",
    "📥 Uploading to cloud... Backup + main server in sync.",
    "🎬 Episode drop incoming... Stay ready!",
    "🔥 Massive upload ongoing... Full season content coming soon.",
    "📦 Packaging completed... Uploading final files now.",
    "🎉 Release almost done... Get ready to watch!",
    "📤 Uploading HD version... SD version already in queue.",
    "⚡ Fast upload mode enabled... Delivering content quickly.",
    "🧠 Smart encoding active... Optimizing for all devices.",
    "📢 Announcement: Episode upload in progress, links soon!",
    "💥 Big release today... Uploading latest episode now.",
    "📺 Streaming-ready files being prepared... Sit tight!",
    "🎯 Final step... Upload will complete any moment now."
]

# ------------------ SPAM FUNCTION ------------------

async def spam_channel(channel_id: int, context: ContextTypes.DEFAULT_TYPE):
    while True:
        try:
            msg_text = random.choice(MESSAGES)

            await context.bot.send_message(
                chat_id=channel_id,
                text=msg_text
            )

            await asyncio.sleep(30)

        except asyncio.CancelledError:
            break
        except Exception as e:
            print(f"[SPAM ERROR] {e}")
            await asyncio.sleep(5)

# ------------------ COMMAND: START ------------------

async def sahu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        channel_id = int(context.args[0])

        if channel_id in spam_tasks:
            await update.message.reply_text("Already running.")
            return

        spam_task = asyncio.create_task(
            spam_channel(channel_id, context)
        )
        spam_tasks[channel_id] = spam_task

        await update.message.reply_text(f"Started in {channel_id}")

    except:
        await update.message.reply_text("Usage: /sahu -100xxxx")

# ------------------ COMMAND: STOP ------------------

async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        channel_id = int(context.args[0])

        if channel_id in spam_tasks:
            spam_tasks[channel_id].cancel()
            del spam_tasks[channel_id]
            await update.message.reply_text("Stopped successfully.")
        else:
            await update.message.reply_text("Not running.")

    except:
        await update.message.reply_text("Usage: /stop -100xxxx")

# ------------------ MAIN ------------------

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("sahu", sahu))
    app.add_handler(CommandHandler("stop", stop))

    print("Bot Running...")
    app.run_polling()

if __name__ == "__main__":
    main()