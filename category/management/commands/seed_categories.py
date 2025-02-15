# your_app/management/commands/seed_categories.py

from django.core.management.base import BaseCommand
from django.utils.text import slugify
from category.models import Category # replace 'your_app' with your actual app name

class Command(BaseCommand):
    help = 'Seed the categories database with initial data'

    def handle(self, *args, **options):
        # Main categories with their direct components
        categories = {
        "Engine Components": [
            "Cylinder block", "Cylinder head", "Crankshaft", "Camshaft", 
            "Pistons and rings", "Connecting rods", "Valves and valve springs",
            "Timing belt/chain", "Oil pump", "Air filter", "Fuel filter",
            "Oil filter", "Spark plugs", "Ignition coils", "Fuel injectors",
            "Turbocharger/Supercharger", "Intake/exhaust manifolds", "Engine mounts"
        ],
        "Transmission System": [
            "Clutch assembly", "Gearbox", "Gear shifter", "Synchronizer rings",
            "Transmission fluid", "Drive shaft", "Universal joints", "Torque converter",
            "Transmission solenoids", "Valve body", "Planetary gear set",
            "Transmission bands", "ATF fluid and filter"
        ],
        "Electrical System": [
            "Starter motor", "Alternator", "Battery", "Voltage regulator",
            "Headlights", "Tail lights", "Turn signals", "Fog lamps",
            "Interior lights", "Light bulbs", "ECU (Engine Control Unit)",
            "Sensors (oxygen, temperature, pressure)", "Fuses and relays",
            "Wiring harness", "Control modules"
        ],
        "Brake System": [
            "Master cylinder", "Brake lines", "Brake fluid", "Wheel cylinders",
            "Brake calipers", "Brake pads", "Brake shoes", "Brake rotors/discs",
            "Brake drums", "ABS module", "ABS sensors", "ABS pump"
        ],
        "Suspension and Steering": [
            "Shock absorbers", "Struts", "Springs (coil, leaf)", "Control arms",
            "Ball joints", "Bushings", "Sway bars", "Steering rack",
            "Power steering pump", "Steering column", "Tie rods",
            "Steering knuckle", "Power steering fluid"
        ],
        "Cooling System": [
            "Radiator assembly", "Water pump", "Thermostat", "Cooling fan",
            "Coolant reservoir", "Hoses and clamps", "Temperature sensors"
        ],
        "Fuel System": [
            "Fuel pump", "Fuel tank", "Fuel lines", "Fuel pressure regulator",
            "Air filter housing", "Mass air flow sensor", "Throttle body",
            "Intake manifold"
        ],
        "Exhaust System": [
            "Catalytic converter", "Muffler", "Exhaust manifold", "Oxygen sensors",
            "Exhaust pipes", "Hangers and clamps", "DPF (Diesel Particulate Filter)"
        ],
        "Body Parts": [
            "Bumpers", "Fenders", "Hood", "Doors", "Trunk/boot lid",
            "Side mirrors", "Grille", "Window glass", "Dashboard", "Seats",
            "Door panels", "Carpet", "Headliner", "Center console", "Safety belts"
        ],
        "HVAC System": [
            "Air conditioning compressor", "Condenser", "Evaporator",
            "Expansion valve", "Blower motor", "Heater core",
            "AC lines and hoses", "Cabin air filter"
        ],
        "Wheels and Tires": [
            "Rims", "Wheel bearings", "Hub assembly", "Lug nuts/bolts",
            "Tires", "Tire valves", "TPMS sensors", "Wheel weights"
        ]
    }
        
        for main_category, components in categories.items():
            # Create main category
            main_cat, created = Category.objects.get_or_create(
                name=main_category,
                slug=slugify(main_category),
                parent=None
            )
            
            if created:
                self.stdout.write(f'Created main category: {main_category}')
            
            # Create components under the main category
            for component in components:
                _, created = Category.objects.get_or_create(
                    name=component,
                    slug=slugify(f"{component}"),
                    parent=main_cat
                )
                
                if created:
                    self.stdout.write(f'Created component: {component}')