from setuptools import setup

dependencies = [
    "blspy==1.0.2",  # Signature library
    "chiavdf==1.0.1",  # timelord and vdf verification
    "chiabip158==1.0",  # bip158-style wallet filters
    "chiapos==1.0.2",  # proof of space
    "clvm==0.9.6",
    "clvm_rs==0.1.7",
    "clvm_tools==0.4.3",
    "aiohttp==3.7.4",  # HTTP server for full node rpc
    "aiosqlite==0.17.0",  # asyncio wrapper for sqlite, to store blocks
    "bitstring==3.1.7",  # Binary data management library
    "colorlog==5.0.1",  # Adds color to logs
    "concurrent-log-handler==0.9.19",  # Concurrently log and rotate logs
    "cryptography==3.4.7",  # Python cryptography library for TLS - keyring conflict
    "keyring==23.0.1",  # Store keys in MacOS Keychain, Windows Credential Locker
    "keyrings.cryptfile==1.3.4",  # Secure storage for keys on Linux (Will be replaced)
    #  "keyrings.cryptfile==1.3.8",  # Secure storage for keys on Linux (Will be replaced)
    #  See https://github.com/frispete/keyrings.cryptfile/issues/15
    "PyYAML==5.4.1",  # Used for config file format
    "setproctitle==1.2.2",  # Gives the thyme processes readable names
    "sortedcontainers==2.3.0",  # For maintaining sorted mempools
    "websockets==8.1.0",  # For use in wallet RPC and electron UI
    "click==7.1.2",  # For the CLI
    "dnspython==2.1.0",  # Query DNS seeds
]

upnp_dependencies = [
    "miniupnpc==2.1",  # Allows users to open ports on their router
]

dev_dependencies = [
    "pytest",
    "pytest-asyncio",
    "flake8",
    "mypy",
    "black",
    "aiohttp_cors",  # For blackd
    "ipython",  # For asyncio debugging
]

kwargs = dict(
    name="thyme-blockchain",
    author="Mariano Sorgente",
    author_email="mariano@thymenetwork.org",
    description="Thyme blockchain full node, farmer, timelord, and wallet.",
    url="https://thymenetwork.org/",
    license="Apache License",
    python_requires=">=3.7, <4",
    keywords="thyme blockchain node",
    install_requires=dependencies,
    setup_requires=["setuptools_scm"],
    extras_require=dict(
        uvloop=["uvloop"],
        dev=dev_dependencies,
        upnp=upnp_dependencies,
    ),
    packages=[
        "build_scripts",
        "thyme",
        "thyme.cmds",
        "thyme.consensus",
        "thyme.daemon",
        "thyme.full_node",
        "thyme.timelord",
        "thyme.farmer",
        "thyme.harvester",
        "thyme.introducer",
        "thyme.plotting",
        "thyme.protocols",
        "thyme.rpc",
        "thyme.server",
        "thyme.simulator",
        "thyme.types.blockchain_format",
        "thyme.types",
        "thyme.util",
        "thyme.wallet",
        "thyme.wallet.puzzles",
        "thyme.wallet.rl_wallet",
        "thyme.wallet.cc_wallet",
        "thyme.wallet.did_wallet",
        "thyme.wallet.settings",
        "thyme.wallet.trading",
        "thyme.wallet.util",
        "thyme.ssl",
        "mozilla-ca",
    ],
    entry_points={
        "console_scripts": [
            "thyme = thyme.cmds.thyme:main",
            "thyme_wallet = thyme.server.start_wallet:main",
            "thyme_full_node = thyme.server.start_full_node:main",
            "thyme_harvester = thyme.server.start_harvester:main",
            "thyme_farmer = thyme.server.start_farmer:main",
            "thyme_introducer = thyme.server.start_introducer:main",
            "thyme_timelord = thyme.server.start_timelord:main",
            "thyme_timelord_launcher = thyme.timelord.timelord_launcher:main",
            "thyme_full_node_simulator = thyme.simulator.start_simulator:main",
        ]
    },
    package_data={
        "thyme": ["pyinstaller.spec"],
        "thyme.wallet.puzzles": ["*.clvm", "*.clvm.hex"],
        "thyme.util": ["initial-*.yaml", "english.txt"],
        "thyme.ssl": ["thyme_ca.crt", "thyme_ca.key", "dst_root_ca.pem"],
        "mozilla-ca": ["cacert.pem"],
    },
    use_scm_version={"fallback_version": "unknown-no-.git-directory"},
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
)


if __name__ == "__main__":
    setup(**kwargs)
