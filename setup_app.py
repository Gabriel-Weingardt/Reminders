from setuptools import setup
OPTIONS = {"iconfile":"Checkbook.icns"}
setup(
    app=["Reminders.py"],
    name="Reminder",
    options={"py2app":OPTIONS},
    setup_requires=["py2app"],
)
