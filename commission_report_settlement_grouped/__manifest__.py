# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Commission Report Settlement Grouped",
    "summary": "Adds new settlement report that groups lines by invoice.",
    "version": "15.0.1.0.0",
    "category": "Commissions",
    "website": "https://github.com/sygel-technology/sy-commission",
    "author": "Sygel",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "account_commission",
    ],
    "data": [
        "report/commission_report_settlement_grouped.xml",
    ],
}
