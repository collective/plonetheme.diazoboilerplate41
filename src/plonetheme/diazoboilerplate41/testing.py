from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

import plonetheme.diazoboilerplate41


PLONETHEME_DIAZOBOILERPLATE41 = PloneWithPackageLayer(
    zcml_package=plonetheme.diazoboilerplate41,
    zcml_filename='testing.zcml',
    name="PLONETHEME_DIAZOBOILERPLATE41")

PLONETHEME_DIAZOBOILERPLATE41_INTEGRATION = IntegrationTesting(
    bases=(PLONETHEME_DIAZOBOILERPLATE41, ),
    name="PLONETHEME_DIAZOBOILERPLATE41_INTEGRATION")

PLONETHEME_DIAZOBOILERPLATE41_FUNCTIONAL = FunctionalTesting(
    bases=(PLONETHEME_DIAZOBOILERPLATE41, ),
    name="PLONETHEME_DIAZOBOILERPLATE41_FUNCTIONAL")
