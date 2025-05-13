import frappe
import requests

def check_backup_event(doc, method):
    if doc.method != "take_backups_over_google_drive":
        return

    if doc.status != "Success":
        return

    url_doc = frappe.get_all("Kuma URL Config", fields=["kuma_push_url"])
    if url_doc and url_doc[0].kuma_push_url:
        try:
            response = requests.get(url_doc[0].kuma_push_url)
            frappe.logger().info(f"Kuma URL triggered: {response.status_code}")
        except Exception as e:
            frappe.logger().error(f"Failed to trigger Kuma URL: {e}")
