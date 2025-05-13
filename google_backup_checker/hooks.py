app_name = "google_backup_checker"
app_title = "Google Backup Checker"
app_publisher = "Your Name"
app_description = "Triggers Kuma on GDrive backup"
app_email = "your@email.com"
app_license = "MIT"

doc_events = {
    "Scheduled Job Log": {
        "on_update": "google_backup_checker.events.backup_trigger.check_backup_event"
    }
}
