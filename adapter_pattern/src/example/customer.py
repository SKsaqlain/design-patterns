from dataclasses import dataclass


# --- Unified Data Model ---
# Common representation of a customer across all CRM systems.
# Each adapter maps its CRM-specific fields into this standard format.
@dataclass
class Customer():
    id: str
    full_name: str
    email: str
    status: str
