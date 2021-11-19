# Ransomware Research
![](https://cdn-images-1.medium.com/fit/t/1600/480/1*zSPtMkp70YN9JDhFRaHHXA.jpeg)
Purely educational research

## Notes
  1. This is only meant to be used for a very specific case study as part of my studies with Unitec Institute of Technology
  2. Everything here assumes that this entire repository has been downloaded via a backdoor
  3. This repository should be placed in the directory that contains the files that are to be encrypted or decrypted
  4. At the moment, only `html` files are handled
  5. The key for decryption is saved on the victim's machine once `key_generator.py` is run. DO NOT DELETE once it is generated. Keep it stored on the victim's machine (remember, this isn't the real thing, demo only), or copy it to another machine for future decryption

## Instructions
  1. Instructions can be generated in terminal using: `python RWResearch/basicrypt.py --h`
  2. Generate a key to lock the file/s you want locked running the following: `python RWResearch/attacker/key_generator.py`
  3. Select a file you want encrypted using: `python RWResearch/basicrypt.py -e key.key file_to_be_encrypted`
  4. To decrypt, use `python RWResearch/basicrypt.py -d key.key file_to_be_decrypted`

## Ideas to try/improve on
* Use asymmetric key
* Handle errors for wrong input
* Encrypt any kind of file, while being able to recover the correct file type when decrypting
* Instead of defacing the site, create a duplicate that uploads the ransomware to legitimate customers
* A better idea around using the key on the victim machine that ensures it's only used by the attacker
* Add some `this looks like a legit hacking tool` terminal art when running the tool (maybe progress bar, etc) for the lolz
* For the deface page, instead of a gif to download, link to a url that can play as the background and overlay text on top
