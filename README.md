<h1> HL7 Message Generation </h1>

This repository contains a suite of Python scripts designed to generate realistic HL7 test messages for healthcare application development. The scripts support various HL7 message types and are crafted to adhere to HL7 standards.

<h2> Overview </h2>

The HL7 Message Generation suite consists of the following components:

<li>main.py: An interactive script that orchestrates the message generation process.</li>
<li>message_generation.py: Generates full HL7 messages based on user input.</li>
<li>segment_generation.py: Creates individual HL7 message segments with realistic data.</li>
<li>utilities.py: Provides utility functions for data generation used across the suite.</li>
<li>reference_data.py: Provides a file to add scenario specific data</li>

<h2> Getting Started </h2>

<p> To use this message generation suite, you'll need Python installed on your system. Clone the repository, navigate to the directory, and run the main.py script: </p>

```git clone https://github.com/dcpluard/HL7-Message-Generator```

```cd hl7-message-generation-suite```

```python main.py```

Follow the prompts to specify the message type and event type you want to generate.

<h2> Prerequisites </h2>

<li>Python 3.x</li>
<li>`hl7apy`</li>
<li>`faker`</li>

<p> Make sure all dependencies are installed:</p>

```pip install -r requirements.txt```

<h2> Usage </h2>
<p>Run the ```main.py script``` and enter the message type and event type as prompted. The script will output the generated HL7 message to the console and, if desired, to a file.</p>

```python main.py```

<h2> Acknowledgments </h2>

<li> <a href="https://pypi.org/project/hl7apy/">hl7apy</a> for providing the core HL7 API.</li>
<li> <a href="https://pypi.org/project/Faker/0.7.4/">Faker</a> for generating realistic data.</li>
