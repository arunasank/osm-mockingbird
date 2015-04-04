# -*- coding: utf-8 -*-
import overpy
import json
from osmapi import OsmApi
import transliteration

#utf line added to allow for usage of utf-8 characters present in Indic languages while writing strings
#overpy - used to retrieve the nodes in a JSON format using the python wrapper for Overpass
#osmapi - used to automate updations to OSM
#transliteration - used for Indic to Indic language transliteration

#get an instance of the Transliterator - Initialise transliterator
kannadaToTamizhTransliterator = transliteration.Transliterator()
#Initialise overpyAPI
overpyAPI = overpy.Overpass()
#Initialise osmapi - Replace the value in username with your username. 
#Replace the value in password with your password
myOSMAPI = OsmApi(username="Arunasank", password="********")

#retrieve the result nodes using overpass for the Rajajinagar bounding box
resultNodes = overpyAPI.query("[out:json];node(12.9936,77.549,12.99651,77.55526);out;")

#Iterate through all the nodes in the result
for i in resultNodes.nodes:
	#filter nodes having tags
	if(i.tags):
		tag = i.tags
		#if Kannada tag(Or any other Indic Tag) is present, filter once more
		if("name:kn" in tag.keys()):
			#transliterate value in tag to required Indic language
			tag["name:ta"] = kannadaToTamizhTransliterator.transliterate_indic_indic(tag["name:kn"],"kn_IN","ta_IN")
			#store the result in a new JSON
			nodeJSON = {}
			nodeJSON["id"] = i.id
			nodeJSON["lat"] = i.lat
			nodeJSON["lon"] = i.lon
			nodeJSON["version"] = 8
			nodeJSON["tag"] = i.tags
			#update Node according to osmapi guidelines -1) Create changeset 2) Update node 3)Close changeset
			myOSMAPI.ChangesetCreate({u"comment": u"Automating Transliteration"})
			myOSMAPI.NodeUpdate(nodeJSON)
			myOSMAPI.ChangesetClose()
