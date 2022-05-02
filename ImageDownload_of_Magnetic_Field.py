from spider import download_img


def Magnetic_ImageDownload() -> None:
    """Download some images of Magnetic Field of Earth in 2020."""

    download_img(['https://wdc.kugi.kyoto-u.ac.jp/igrf/anime/16-20.gif',
                  'Animation of secular variation in geomagnetic total intensity for the last 400 years.gif'])

    download_img(['https://wdc.kugi.kyoto-u.ac.jp/igrf/map/f-m.gif',
                  'Total Intensity of Magnetic Field.gif'])

    download_img(['https://wdc.kugi.kyoto-u.ac.jp/igrf/map/d-m.gif',
                  'Declination of Magnetic Field.gif'])

    download_img(['https://wdc.kugi.kyoto-u.ac.jp/igrf/map/i-m.gif',
                  'Inclination of Magnetic Field.gif'])

    download_img(['https://wdc.kugi.kyoto-u.ac.jp/igrf/map/h-m.gif',
                  'Horizontal Component of Magnetic Field.gif'])

    download_img(['https://wdc.kugi.kyoto-u.ac.jp/igrf/map/z-m.gif',
                  'Vertical Component of Magnetic Field.gif'])

    download_img(['https://wdc.kugi.kyoto-u.ac.jp/igrf/map/x-m.gif',
                  'Northward Component of Magnetic Field.gif'])

    download_img(['https://wdc.kugi.kyoto-u.ac.jp/igrf/map/y-m.gif',
                  'Eastward Component of Magnetic Field.gif'])
