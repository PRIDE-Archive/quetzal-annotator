"""
Quetzal Annotator - A peptide fragment ion spectrum annotation tool.

Quetzal is a peptide fragment ion spectrum annotation tool to assist researchers 
in annotating and examining tandem mass spectra to ensure that they correctly 
support study conclusions. Quetzal annotates spectra using the new Human Proteome 
Organization (HUPO) Proteomics Standards Initiative (PSI) mzPAF standard for 
fragment ion peak annotation.

This package provides:
- Spectrum annotation and analysis
- Peptidoform processing with ProForma notation support
- Universal Spectrum Identifier (USI) validation
- Mass spectrometry ontology handling
- Publication-quality spectrum visualization
"""

__version__ = "0.1.0"
__author__ = "Quetzal Annotator Team"
__email__ = "quetzal-annotator@example.com"

# Import main classes for easy access
from .spectrum import Spectrum
from .spectrum_annotator import SpectrumAnnotator
from .spectrum_examiner import SpectrumExaminer
from .spectrum_comparator import SpectrumComparator
from .peptidoform import Peptidoform
from .proforma_peptidoform import ProformaPeptidoform
from .universal_spectrum_identifier import UniversalSpectrumIdentifier
from .universal_spectrum_identifier_validator import UniversalSpectrumIdentifierValidator
from .ontology import Ontology
from .ontology_collection import OntologyCollection
from .ontology_term import OntologyTerm
from .mass_reference import MassReference
from .response import Response

__all__ = [
    "Spectrum",
    "SpectrumAnnotator", 
    "SpectrumExaminer",
    "SpectrumComparator",
    "Peptidoform",
    "ProformaPeptidoform",
    "UniversalSpectrumIdentifier",
    "UniversalSpectrumIdentifierValidator",
    "Ontology",
    "OntologyCollection", 
    "OntologyTerm",
    "MassReference",
    "Response",
] 