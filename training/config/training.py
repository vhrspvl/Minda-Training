from __future__ import unicode_literals
from frappe import _
import frappe


def get_data():
    system_manager = frappe.get_doc("User", frappe.session.user).get(
        "roles", {"role": "System Manager"})
    training_manager = frappe.get_doc("User", frappe.session.user).get(
        "roles", {"role": "Training Manager"})
    employee = frappe.get_doc("User", frappe.session.user).get(
        "roles", {"role": "Employee"})
    hr_manager = frappe.get_doc("User", frappe.session.user).get(
        "roles", {"role": "HR Manager"})
    if system_manager:
        return [
             {
                "label": _("Evaluation Forms"),
                "items": [
                    {
                        "type": "doctype",
                        "name": "Auto Cutting and Crimping",
                        "description": _("Auto Cutting and Crimping"),
                    },
                    {
                        "type": "doctype",
                        "name": "Semi Auto Crimping",
                        "description": _("Semi Auto Crimping"),
                    },
                    {
                        "type": "doctype",
                        "name": "Assembly Evaluation",
                        "description": _("Assembly Evaluation"),
                    }, 
                    {
                        "type": "doctype",
                        "name": "Quality Evaluation",
                        "description": _("Quality Evaluation"),
                    },                 
                ]
            },
            {
                "label": _("Monitoring Sheets"),
                "items": [
                    {
                        "type": "doctype",
                        "name": "Associate Performance Monitoring",
                        "description": _("Associate Performance Monitoring"),
                    },
                    {
                        "type": "doctype",
                        "name": "Associate Performance Monitoring Check Sheet",
                        "description": _("Associate Performance Monitoring Check Sheet"),
                    },
                    {
                        "type": "doctype",
                        "name": "Knowledge Verification Sheet",
                        "description": _("Knowledge Verification Sheet"),
                    },
                    {
                        "type": "doctype",
                        "name": "Employee Performance Summary Report",
                        "description": _("Employee Performance Summary Report"),
                    }
                ]
            },
            {
                "label": _("Tests & Questions"),
                "items": [
                    {
                        "type": "doctype",
                        "name": "Color Blindness Test",
                        "description": _("Color Blindness Test"),
                    },
                    {
                        "type": "doctype",
                        "name": "Selection Test",
                        "description": _("Selection Test"),
                    },
                    {
                        "type": "doctype",
                        "name": "New Joinees Practical Knowledge Verification",
                        "description": _("New Joinees Practical Knowledge Verification"),
                    },
                    {
                        "type": "doctype",
                        "name": "Induction Training Assembly Area",
                        "description": _("Induction Training Assembly Area"),
                    },
                    {
                        "type": "doctype",
                        "name": "Induction Training Machine Area Crimping",
                        "description": _("Induction Training Machine Area Crimping"),
                    },
                    {
                        "type": "doctype",
                        "name": "Induction Training Machine Area Operator",
                        "description": _("Induction Training Machine Area Operator"),
                    },
                    
                    {
                        "type": "doctype",
                        "name": "Crimping Questions",
                        "description": _("Crimping Questions"),
                    }
                ]
            },
            {
                "label": _("Tools & Reports"),
                "items": [
                    {
                        "type": "report",
                        "is_query_report": True,
                        "name": "New Joinees Details",
                        "label": _("New Joinees Test Details"),
                        "description": _("New Joinees Details"),
                        "doctype": "Employee"
                    },
                    {
                        "type": "report",
                        "is_query_report": True,
                        "name": "Pending List KVS",
                        "label": _("Pending List KVS"),
                        "description": _("Pending List KVS"),
                        "doctype": "Employee"
                    },
                    {
                        "type": "report",
                        "is_query_report": True,
                        "name": "Practical Knowledge Verification Pending List",
                        "label": _("Pending List Practical Knowledge Verification"),
                        "description": _("Pending List KVS"),
                        "doctype": "New Joinees Practical Knowledge Verification"
                    },
                    {
                        "type": "doctype",
                        "name": "KVS Type Assignment",
                        "description": _("Line and Shift Assignment Details"),
                    },
                    {
                        "type": "doctype",
                        "name": "Line and Shift Assignment Tool",
                        "description": _("Line and Shift Assignment Tool"),
                    },
                    {
                        "type": "doctype",
                        "name": "Line and Shift Assignment Details",
                        "description": _("Line and Shift Assignment Details"),
                    },
                    {
                        "type": "report",
                        "is_query_report": True,
                        "name": "Skill Evaluation Due Report",
                        "label": _("Skill Evaluation Due Report"),
                        "description": _("Skill Evaluation Due Report")
                        # "doctype": "New Joinees Practical Knowledge Verification"
                    }
                ]
            },
             {
                "label": _("Supervisor Evaluation Marks"),
                "items": [
                     {
                        "type": "doctype",
                        "name": "Auto Cutting and Crimping Marks",
                        "description": _("Auto Cutting and Crimping Marks"),
                    },
                    {
                        "type": "doctype",
                        "name": "Semi Auto Crimping Marks",
                        "description": _("Semi Auto Crimping Marks"),
                    },
                    {
                        "type": "doctype",
                        "name": "Assembly Evaluation Marks",
                        "description": _("Assembly Evaluation Marks"),
                    },
                    {
                        "type": "doctype",
                        "name": "Quality Evaluation Marks",
                        "description": _("Quality Evaluation Marks"),
                    },
                ]
            },
        ]
    elif training_manager:
        return [
            {
                "label": _("Evaluation Forms"),
                "items": [
                    {
                        "type": "doctype",
                        "name": "Auto Cutting and Crimping",
                        "description": _("Auto Cutting and Crimping"),
                    },
                    {
                        "type": "doctype",
                        "name": "Semi Auto Crimping",
                        "description": _("Semi Auto Crimping"),
                    },
                    {
                        "type": "doctype",
                        "name": "Assembly Evaluation",
                        "description": _("Assembly Evaluation"),
                    }, 
                    {
                        "type": "doctype",
                        "name": "Quality Evaluation",
                        "description": _("Quality Evaluation"),
                    },                 
                ]
            },
            {
                "label": _("Monitoring Sheets"),
                "items": [
                     {
                        "type": "doctype",
                        "name": "Associate Performance Monitoring",
                        "description": _("Associate Performance Monitoring"),
                    },
                    {
                        "type": "doctype",
                        "name": "Associate Performance Monitoring Check Sheet",
                        "description": _("Associate Performance Monitoring Check Sheet"),
                    },
                    {
                        "type": "doctype",
                        "name": "Knowledge Verification Sheet",
                        "description": _("Knowledge Verification Sheet"),
                    },
                    {
                        "type": "doctype",
                        "name": "Employee Performance Summary Report",
                        "description": _("Employee Performance Summary Report"),
                    }
                ]
            },
            {
                "label": _("Tests & Questions"),
                "items": [
                    {
                        "type": "doctype",
                        "name": "Color Blindness Test",
                        "description": _("Color Blindness Test"),
                    },
                    {
                        "type": "doctype",
                        "name": "Selection Test",
                        "description": _("Selection Test"),
                    },
                    {
                        "type": "doctype",
                        "name": "New Joinees Practical Knowledge Verification",
                        "description": _("New Joinees Practical Knowledge Verification"),
                    },
                    {
                        "type": "doctype",
                        "name": "Induction Training Assembly Area",
                        "description": _("Induction Training Assembly Area"),
                    },
                    {
                        "type": "doctype",
                        "name": "Induction Training Machine Area Crimping",
                        "description": _("Induction Training Machine Area Crimping"),
                    },
                    {
                        "type": "doctype",
                        "name": "Induction Training Machine Area Operator",
                        "description": _("Induction Training Machine Area Operator"),
                    },
                    
                    {
                        "type": "doctype",
                        "name": "Crimping Questions",
                        "description": _("Crimping Questions"),
                    }
                ]
            },
            {
                "label": _("Tools & Reports"),
                "items": [
                    {
                        "type": "report",
                        "is_query_report": True,
                        "name": "New Joinees Details",
                        "label": _("New Joinees Test Details"),
                        "description": _("New Joinees Details"),
                        "doctype": "Employee"
                    },
                    {
                        "type": "report",
                        "is_query_report": True,
                        "name": "Pending List KVs",
                        "label": _("Pending List KVS"),
                        "description": _("Pending List KVS"),
                        "doctype": "Employee"
                    },
                    {
                        "type": "report",
                        "is_query_report": True,
                        "name": "Practical Knowledge Verificatio Pending List",
                        "label": _("Pending List Practical Knowledge Verification"),
                        "description": _("Pending List KVS"),
                        "doctype": "New Joinees Practical Knowledge Verification"
                    },
                    {
                        "type": "doctype",
                        "name": "KVS Type Assignment",
                        "description": _("Line and Shift Assignment Details"),
                    },
                    {
                        "type": "doctype",
                        "name": "Line and Shift Assignment Tool",
                        "description": _("Line and Shift Assignment Tool"),
                    },
                    {
                        "type": "doctype",
                        "name": "Line and Shift Assignment Details",
                        "description": _("Line and Shift Assignment Details"),
                    },
                    {
                        "type": "report",
                        "is_query_report": True,
                        "name": "Skill Evaluation Due Report",
                        "label": _("Skill Evaluation Due Report"),
                        "description": _("Skill Evaluation Due Report")
                        # "doctype": "New Joinees Practical Knowledge Verification"
                    }
                ]
            },
            {
                "label": _("Supervisor Evaluation Marks"),
                "items": [
                     {
                        "type": "doctype",
                        "name": "Auto Cutting and Crimping Marks",
                        "description": _("Auto Cutting and Crimping Marks"),
                    },
                    {
                        "type": "doctype",
                        "name": "Semi Auto Crimping Marks",
                        "description": _("Semi Auto Crimping Marks"),
                    },
                    {
                        "type": "doctype",
                        "name": "Assembly Evaluation Marks",
                        "description": _("Assembly Evaluation Marks"),
                    },
                    {
                        "type": "doctype",
                        "name": "Quality Evaluation Marks",
                        "description": _("Quality Evaluation Marks"),
                    },
                ]
            },
        ]
    elif hr_manager:
        return [
            {
                "label": _("Evaluation Forms"),
                "items": [
                    {
                        "type": "doctype",
                        "name": "Auto Cutting and Crimping",
                        "description": _("Auto Cutting and Crimping"),
                    },
                    {
                        "type": "doctype",
                        "name": "Semi Auto Crimping",
                        "description": _("Semi Auto Crimping"),
                    },
                    {
                        "type": "doctype",
                        "name": "Assembly Evaluation",
                        "description": _("Assembly Evaluation"),
                    }, 
                    {
                        "type": "doctype",
                        "name": "Quality Evaluation",
                        "description": _("Quality Evaluation"),
                    },                 
                ]
            },
            {
                "label": _("Monitoring Sheets"),
                "items": [
                    {
                        "type": "doctype",
                        "name": "Associate Performance Monitoring",
                        "description": _("Associate Performance Monitoring Tool"),
                    },
                    {
                        "type": "doctype",
                        "name": "Associate Performance Monitoring Check Sheet",
                        "description": _("Associate Performance Monitoring Check Sheet"),
                    },
                    {
                        "type": "doctype",
                        "name": "Knowledge Verification Sheet",
                        "description": _("Knowledge Verification Sheet"),
                    },
                    {
                        "type": "doctype",
                        "name": "Employee Performance Summary Report",
                        "description": _("Employee Performance Summary Report"),
                    }
                ]
            },
            {
                "label": _("Tests & Questions"),
                "items": [
                    {
                        "type": "doctype",
                        "name": "Induction Training Assembly Area",
                        "description": _("Induction Training Assembly Area"),
                    },
                    {
                        "type": "doctype",
                        "name": "Induction Training Machine Area Crimping",
                        "description": _("Induction Training Machine Area Crimping"),
                    },
                    {
                        "type": "doctype",
                        "name": "Induction Training Machine Area Operator",
                        "description": _("Induction Training Machine Area Operator"),
                    },
                    {
                        "type": "doctype",
                        "name": "Crimping Questions",
                        "description": _("Crimping Questions"),
                    }
                ]
            },
        ]
    
