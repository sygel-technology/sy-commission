import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-sygel-technology-sy-commission",
    description="Meta package for sygel-technology-sy-commission Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-commission_report_settlement_font_size>=15.0dev,<15.1dev',
        'odoo-addon-commission_report_settlement_grouped>=15.0dev,<15.1dev',
        'odoo-addon-commission_settlement_line_percentage>=15.0dev,<15.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 15.0',
    ]
)
