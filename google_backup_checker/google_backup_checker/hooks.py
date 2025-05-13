app_name = "google_backup_checker"
app_title = "Google Backup Checker"
app_publisher = "Your Name"
app_description = "App to trigger Kuma on GDrive backup"
app_email = "email@example.com"
app_license = "MIT"

app_include_js = "/assets/google_backup_checker/js/google_backup_checker.js"

doc_events = {
    "Scheduled Job Log": {
        "on_update": "google_backup_checker.events.backup_trigger.check_backup_event"
    }
}
