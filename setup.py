from setuptools import setup


setup(
    name='cldfbench_grammaticon',
    py_modules=['cldfbench_grammaticon'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'grammaticon=cldfbench_grammaticon:Dataset',
        ]
    },
    install_requires=[
        'cldfbench',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
