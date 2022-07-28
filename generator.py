
data = {
    "date": "July 27, 2022",
    "num-dacs": 7,
    "aff-units": 4,
    "avg-burden-pct": "87.5%",
    "tracts": [{"id": "0100023023423", "city": "Coronado", "state": "California", "population": "10334.0", "county": "San Diego County",
                "qct-status": "Eligible", "qct-mark": "good", "dac-status": "Disadvantaged", "dac-mark": "good"},
{"id": "0100023023423", "city": "Chicago", "state": "California", "population": "10334.0", "county": "San Diego County",
                "qct-status": "Eligible", "qct-mark": "good", "dac-status": "Disadvantaged", "dac-mark": "bad"}
                ]
}

import base64
with open("map.png", 'rb') as f:
    encoded_string = base64.b64encode(f.read())
    data["map"] = encoded_string.decode('utf-8')
    data["map"] = '<img src="data:image/png;base64,{0}" class="w-full h-auto">'.format(data["map"])

def generate_from_data(data, out_path="out.pdf"):
    tracts_html = "\n".join([
        f"""
        <section class="break-before">
        <div class="h-8 w-full">&nbsp;</div>
        <div class="font-bold text-xl text-white bg-[#00583C] p-2 w-80">Census Tract {tract['id']}</div>
        <div class="text-lg mt-2">
            <div class="inline-block align-top mr-8">
            <b>City:</b> {tract['city']}</br>
            <b>County:</b> {tract['county']}</br>
            <b>State:</b> {tract['state']}</br>
            <b>Population:</b> {tract['population']} </br>
            </div>
            <div class="inline-block align-top">
            <b>QCT Status:</b> <mark class="{tract['qct-mark']}">{tract['qct-status']}</mark></br>
            <b>DAC Status:</b> <mark class="{tract['dac-mark']}">{tract['dac-status']}</mark></br>
            <b>State Percentage:</b> <mark class="bad">90%</mark> </br>
            <b>National Percentage:</b> <mark class="good">40%</mark> </br>
            </div>
        </p>

        <table class="mt-4">
            <tr>
            <th>Indicator</th>
            <th class="w-[70%]">Percentile</th>
            </tr>
            <tr>
            <td>Energy Burden</td>
            <td>
                <div class="w-[95%] good-bar"></div>
                <div class="inline-block align-middle">99</div>
            </td>
            </tr>
            <tr>
            <td>Housing Burden</td>
            <td>
                <div class="w-[35%] bad-bar"></div>
                <div class="inline-block align-middle">25</div>
            </td>
            </tr>
        </table>

        <div class="font-bold text-xl text-white bg-[#69BE28] p-2 w-full mt-8">Property: Lone Bluff View Apartments</div>
        <div class="text-lg mt-2">
            <div class="inline-block align-top mr-8">
            <b>City:</b> Coronado</br>
            <b>County:</b> San Diego County</br>
            <b>State:</b> CA</br>
            <b>Population:</b> 10334.0 </br>
            <b>Population:</b> 10334.0 </br>
            <b>Population:</b> 10334.0 </br>
            <b>Population:</b> 10334.0 </br>
            </div>
            <div class="inline-block align-top">
            <b>City:</b> Coronado</br>
            <b>County:</b> San Diego County</br>
            <b>State:</b> CA</br>
            <b>Population:</b> 10334.0 </br>
            <b>Population:</b> 10334.0 </br>
            <b>Population:</b> 10334.0 </br>
            </div>
        </p>
        </section>
        """
    for tract in data["tracts"] ])

    html = f"""
    <!DOCTYPE html>
    <html>

    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <link href="compiled-styles.css" rel="stylesheet" />
    </head>

    <body class="w-screen">
        <div class="w-full h-fit bg-[#00583C] p-2 px-4 relative">
            <h1 class="text-white font-bold block text-2xl">Equity Tool Report</h1>
            <h1 class="text-white font-bold block text-lg absolute right-4 top-0 pt-2.5">
                {data['date']}
            </h1>
        </div>

        <div class="w-full px-14">
            <section id="main-area " class="w-full h-fit mt-8 text-center">
                <p class="mb-2">
                    <a class="text-black text-xl"><b>Selected Boundary:</b> San Diego County</a
            >
        </p>
        {data['map']}

        <div class="mt-8 w-full h-fit align-top">
            <div class="w-[32%] inline-block">
            <h1 class="font-bold text-4xl"> {data['num-dacs']} </h1>
            <h1 class="font-semibold leading-tight text-lg">DACs </br>  in County</h1>
            </div>
            <div class="w-[32%] h-full inline-block align-top">
            <h1 class="font-bold text-4xl">{data['aff-units']}</h1>
            <h1 class="font-semibold leading-tight text-lg">Affordable </br>  Housing Units</h1>
            </div>
            <div class="w-[32%] inline-block align-top">
            <h1 class="font-bold text-4xl">{data['avg-burden-pct']}</h1>
            <h1 class="font-semibold leading-tight text-lg break-words">Average Energy </br> Burden Percentile</h1>
            </div>
        </div>
        </section>

        {tracts_html}
    </div>
    </body>
    </html>
    """


    import pdfkit
    import subprocess

    options = {
    "enable-local-file-access": None,
    'margin-top': '0in',
    'margin-right': '0in',
    'margin-bottom': '0in',
    'margin-left': '0in'}


    subprocess.call(["lessc", "templates/compiled-styles.css", "templates/simple-styles.css"])
    pdfkit.from_string(html, out_path, options=options, css="templates/simple-styles.css")

generate_from_data(data)