
#---- this script uses the Ollie triplet extractor, thus follows the Ollie Software License Agreement (https://github.com/knowitall/ollie/blob/master/LICENSE)
#---- for the text of the Ollie license see below
#---- this script uses the ReVerb triplet extractor, thus follows the ReVerb Software License Agreement (http://reverb.cs.washington.edu/LICENSE.txt)
#---- for the text of the ReVerb license see below

import requests
import json

class TripletClient(object):
    def __init__(self,url="http://concreteflows.ijs.si/tripletserver/"):
        self.base_url = url

    @property
    def base_url(self):
        return self._base_url

    @base_url.setter
    def base_url(self, value):
        self._base_url = value

    def reverb(self,text):
        r = requests.post(self.base_url+"api/reverb/extract",data=json.dumps({"text":text}))
        return r.json()

    def ollie(self,text):
        r = requests.post(self.base_url+"api/ollie/extract",data=json.dumps({"text":text}))
        return r.json()


'''
Ollie Software License Agreement

Ollie Software
(C) 2011-2012, University of Washington.  All rights reserved.
US patent number 7,877,343 and 12/970,155 patent pending

The University of Washington (UW), Professor Mausam, Michael Schmitz, Robert
Bart, and Stephen Soderland, (Developers) give permission for you and your
laboratory (University) to use Ollie. Ollie is a system that extracts
relational triples from text. Ollie is protected by a United States copyright
and patents. The National Science Foundation supported work on Ollie. Under
University of Washington's patents 7,877,343 (issued) and 12/970,155 (patent
pending), the UW grants to you the non-exclusive right to use patent claims
practiced by the University of Washington's Ollie software solely for
non-commercial purposes and as long as you comply with the terms of this Ollie
Software License Agreement.  UW and the Developers allow you to copy and modify
Ollie for non-commercial purposes, and to distribute modifications through
GitHub or directly to the University of Washington, on the following
conditions:


1.  Ollie is not used for any commercial purposes, or as part of a system
which has commercial purposes.


2.  Any software derived from Ollie must carry prominent notices stating that
you modified it along with the date modified.  The derivative must also carry
prominent notices stating that it is released under this Ollie Software
License Agreement

If you wish to obtain Ollie or to obtain any patent rights for any commercial
purposes, you will need to contact the University of Washington to see if
rights are available and to negotiate a commercial license and pay a fee. This
includes, but is not limited to, using Ollie to provide services to outside
parties for a fee. In that case please contact:

    UW Center for Commercialization
    University of Washington
    4311 11th Ave. NE,
    Suite 500 Seattle, WA 98105-4608

    Phone: (206) 543-3970
    Email: license@u.washington.edu


3. You retain in Ollie and any modifications to Ollie, the copyright,
trademark, patent or other notices pertaining to Ollie as provided by UW.


4. You provide the Developers with feedback on the use of the Ollie software
in your research, and that the Developers and UW are permitted to use any
information you provide in making changes to the Ollie software. All bug
reports and technical questions shall be sent to: afader@cs.washington.edu.
Modifications may be communicated through GitHub pull requests at:

    https://github.com/knowitall/


5. You acknowledge that the Developers, UW and its licensees may develop
modifications to Ollie that may be substantially similar to your modifications
of Ollie, and that the Developers, UW and its licensees shall not be
constrained in any way by you in UW's or its licensees' use or management of
such modifications. You acknowledge the right of the Developers and UW to
prepare and publish modifications to Ollie that may be substantially similar
or functionally equivalent to your modifications and improvements, and if you
obtain patent protection for any modification or improvement to Ollie you
agree not to allege or enjoin infringement of your patent by the Developers,
the UW or by any of UW's licensees obtaining modifications or improvements to
Ollie from the University of Washington or the Developers.


6. If utilization of the Ollie software results in outcomes which will be
published, please specify the version of Ollie you used and cite the UW
Developers.

  @inproceedings{ollie-emnlp12,
      author = {Mausam and Michael Schmitz and Robert Bart and
          Stephen Soderland and Oren Etzioni},
      title = {Open Language Learning for Information Extraction},
      booktitle = {Proceedings of Conference on Empirical Methods in
          Natural Language Processing and Computational Natural
          Language Learning (EMNLP-CONLL)},
      year = {2012}
  }


7. Any risk associated with using the Ollie software at your organization is
with you and your organization. Ollie is experimental in nature and is made
available as a research courtesy "AS IS," without obligation by UW to provide
accompanying services or support.


UW AND THE AUTHORS EXPRESSLY DISCLAIM ANY AND ALL WARRANTIES REGARDING THE
SOFTWARE, WHETHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO WARRANTIES
PERTAINING TO MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE.
'''

'''
ReVerb Software License Agreement

ReVerb Software
(C) 2011-2012, University of Washington.  All rights reserved.
US patent number 7,877,343 and 12/970,155 patent pending

The University of Washington (UW), Professor Oren Etzioni, Anthony Fader,
Michael Schmitz, Robert Bart, Janara Christensen, and Niranjan Balasubramanian
(Developers) give permission for you and your laboratory (University) to use
ReVerb. ReVerb is a system that extracts relational triples from text. ReVerb
is protected by a United States copyright and patents. The National Science
Foundation supported work on ReVerb. Under University of Washington's
patents 7,877,343 (issued) and 12/970,155 (patent pending), the UW grants to
you the non-exclusive right to use patent claims practiced by the University of
Washington's ReVerb software solely for non-commercial purposes and as long as
you comply with the terms of this ReVerb Software License Agreement.  UW and
the Developers allow you to copy and modify ReVerb for non-commercial purposes,
and to distribute modifications through GitHub or directly to the University of
Washington, on the following conditions:


1.  ReVerb is not used for any commercial purposes, or as part of a system
which has commercial purposes.


2.  Any software derived from ReVerb must carry prominent notices stating that
you modified it along with the date modified.  The derivative must also carry
prominent notices stating that it is released under this ReVerb Software
License Agreement

If you wish to obtain ReVerb or to obtain any patent rights for any commercial
purposes, you will need to contact the University of Washington to see if
rights are available and to negotiate a commercial license and pay a fee. This
includes, but is not limited to, using ReVerb to provide services to outside
parties for a fee. In that case please contact:

    UW Center for Commercialization
    University of Washington
    4311 11th Ave. NE,
    Suite 500 Seattle, WA 98105-4608

    Phone: (206) 543-3970
    Email: license@u.washington.edu


3. You retain in ReVerb and any modifications to ReVerb, the copyright,
trademark, patent or other notices pertaining to ReVerb as provided by UW.


4. You provide the Developers with feedback on the use of the ReVerb software
in your research, and that the Developers and UW are permitted to use any
information you provide in making changes to the ReVerb software. All bug
reports and technical questions shall be sent to: afader@cs.washington.edu.
Modifications may be communicated through GitHub pull requests at:

    https://github.com/knowitall/


5. You acknowledge that the Developers, UW and its licensees may develop
modifications to ReVerb that may be substantially similar to your modifications
of ReVerb, and that the Developers, UW and its licensees shall not be
constrained in any way by you in UW's or its licensees' use or management of
such modifications. You acknowledge the right of the Developers and UW to
prepare and publish modifications to ReVerb that may be substantially similar
or functionally equivalent to your modifications and improvements, and if you
obtain patent protection for any modification or improvement to ReVerb you
agree not to allege or enjoin infringement of your patent by the Developers,
the UW or by any of UW's licensees obtaining modifications or improvements to
ReVerb from the University of Washington or the Developers.


6. If utilization of the ReVerb software results in outcomes which will be
published, please specify the version of ReVerb you used and cite the UW
Developers.

    @inproceedings{Fader11,
      author =   {Anthony Fader and Stephen Soderland and Oren Etzioni},
      title =    {Identifying Relations for Open Information Extraction},
      booktitle =    {Proceedings of the Conference of Empirical Methods
                      in Natural Language Processing ({EMNLP} '11)},
      year =     {2011},
      month =    {July 27-31},
      address =  {Edinburgh, Scotland, UK}
    }


7. Any risk associated with using the ReVerb software at your organization is
with you and your organization. ReVerb is experimental in nature and is made
available as a research courtesy "AS IS," without obligation by UW to provide
accompanying services or support.


UW AND THE AUTHORS EXPRESSLY DISCLAIM ANY AND ALL WARRANTIES REGARDING THE
SOFTWARE, WHETHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO WARRANTIES
PERTAINING TO MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE.
'''
