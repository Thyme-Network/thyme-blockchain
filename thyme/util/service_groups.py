from typing import KeysView, Generator

SERVICES_FOR_GROUP = {
    "all": "thyme_harvester thyme_timelord_launcher thyme_timelord thyme_farmer thyme_full_node thyme_wallet".split(),
    "node": "thyme_full_node".split(),
    "harvester": "thyme_harvester".split(),
    "farmer": "thyme_harvester thyme_farmer thyme_full_node thyme_wallet".split(),
    "farmer-no-wallet": "thyme_harvester thyme_farmer thyme_full_node".split(),
    "farmer-only": "thyme_farmer".split(),
    "timelord": "thyme_timelord_launcher thyme_timelord thyme_full_node".split(),
    "timelord-only": "thyme_timelord".split(),
    "timelord-launcher-only": "thyme_timelord_launcher".split(),
    "wallet": "thyme_wallet thyme_full_node".split(),
    "wallet-only": "thyme_wallet".split(),
    "introducer": "thyme_introducer".split(),
    "simulator": "thyme_full_node_simulator".split(),
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
