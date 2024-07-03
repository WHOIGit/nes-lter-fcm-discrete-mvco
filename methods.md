# CTD Rosette Bottle Sampling on NES-LTER cruises

Samples were collected from the water column at multiple depths using
Niskin bottles on a CTD rosette system. A small number of samples were
collected from the ship's underway science seawater near the surface.
All samples were collected into 2 ml sterile cryovials and stored in a
dark container avoiding exposure to sunlight.

# Sample preservation

Samples were brought into lab and preserved using a 50/50 mix of 25%
Glutaraldehyde and 2% Kolliphor P 188, for a final sample concentration
of 0.125% Glutaraldehyde and 0.01% Kolliphor. Prior to May of 2019,
samples were preserved with only 0.125% Glutaraldehyde. Ten minutes
after addition of preservative and gentle mixing, samples were flash
frozen in liquid nitrogen where they remained until analysis.

#Sample processing

Samples were thawed immediately prior to analysis. Each sample was
pulled by syringe through a 150-micrometer Nitex mesh pre-filter to
avoid aspirating overly large particles that might clog the flow
cytometer. For heterotrophic bacterial analysis, 500 microliters were
placed in a separate tube with 0.5 ul 500x SYBR stain in DMSO (a 1:20
dilution of Invitrogen SYBR Green I Nucleic Acid Gel Stain, 10,000X
concentrate in DMSO). The remainder of the sample was placed back in the
original tube. Bacterial samples were mixed with a vortex genie and
allowed to stain in the dark for at least 10 minutes before analysis.

A ThermoFisher Attune NxT Flow Cytometer equipped with two lasers, green
(532 nm, 100mW) and blue (488 nm, 50mW) was used for analysis. The flow
cytometer focus fluid (sheath) was milli Q water with 3% Sodium chloride
(30 ppt) and 0.1% 2-Phenoxyethanol. For quality control, the Attune flow
cytometer Performance test (bead REF# 4449754) was run at least once per
week and a beads mix (see recipe), was run daily for normalized size
calibration. Instrument cleaning was performed at the end of each
analysis day using 25% Hellmanex III detergent.

Each discrete sample was analyzed with 2-3 different configurations
shown in the table Settings_configuration_history_discrete_analysis. The
specific fcs file used for quantification of each cell type is listed in
the data table. Often multiple cell types were quantified with the same
fcs file. FCS files are provided in zipped files organized by cruise.

#Instrument configuration and calibration

Instrument configuration settings and calibration are provided in the
Settings_configuration_history_discrete_analysis file. The table has a
row for each run type used for each research cruise, showing relevant
instrument settings or major changes in optical filter configuration,
bead runs for calibration, cruise sample collection date, and range of
analysis dates.

Recipe for FCB bead mix:

-100ml salt sheath with 0.1% 2 phenoxyethanol

-400 ul diluted stock 0.5 um beads Polysciences Inc #19507

-5 ul 1 um beads Polysciences Inc #23517

-5 drops invitrogen Alignflow plus flow cytometry alignment beads, 6 um
#C47397

# Data processing

Cells were identified and enumerated from the flow cytometry (.fcs) data
files based on their scattering, SYBR (525 nm), phycoerythrin (575 nm)
and chlorophyll (680 nm) fluorescence signals. Gating was completed
manually in the Attune NXT software interface, yielding Attune NXT
workspace (.aws) files that were exported and interpreted in matlab for
enumeration in the provided data table.

The size of each cell was estimated from side-angle light scattering.
Side scattering signals were normalized using the side scattering signal
of 1-um beads (Flow Check High Intensity Alignment Grade Particles,
Polysciences) which were part of the bead mix that was run daily during
analysis. Bead-normalized scattering signals were converted to cell
volume estimates based on a calibration curve derived from phytoplankton
cultures independently sized on a Coulter Multisizer. Finally, cell
volume was converted to cell carbon following the relationships
described by Menden-Deuer and Lessard (2000). Precision for carbon
concentration is provided to two decimal places. Carbon concentration
for heterotrophic prokaryotes was estimated from cell concentration and
constant carbon per cell ratio of 20fg per cell from Lee and Furham
(1987) who report that bacterial biomass is relatively invariant to cell
size. The selected term, "Heterotrophic prokaryotes" from the Marine
Microbial Flow Cytometry Standardised Group Names, encompasses both
bacteria and archaea, and in some cases overlaps with Prochlorococcus.
For the purposes of this package, we refer to this group as
heterotrophic bacteria.

For all sample runs, the first 20 percent of the volume was omitted from
analysis and cell quantification to avoid underestimation. The volume
analyzed columns account for this adjustment and reflect the true volume
analyzed, rather than the total volume run.

# Quality control

During the manual gating process, if data quality appears poor, gating
information (.aws file) is not exported, and data subsequently are not
reported. Although this is rare, reasons would be obvious Attune
malfunction or lack of preservative. After all manual gates (.aws files)
are exported, they are processed with matlab matching them to
corresponding .fcs files. In this step, we generated a list of fcs files
that did not match to an aws file and ensured the list is as expected.
Next, we cross referenced the list of gated samples with our cruise
sample log and corrected any mistakes; for example if the log indicates
that an alternate niskin was used when that in the filename misfired.
The filenames themselves are unchanged during this manual reassignment,
so the adjustments are trackable by comparing the filenames to the cast
and niskin columns. Finally, we output .pngs of cytograms generated from
the matlab processing of fcs and aws files to check for and correct
gating errors. At each step, we reprocessed as needed.

#Data Package Assembly

We add CTD bottle metadata (time, latitude, longitude, depth, potential
temperature, salinity) from the REST Application Programming Interface
(API) of the NES-LTER data system.

Code for data package assembly, including metadata from templates, is
available on GitHub
(https://github.com/WHOIGit/nes-lter-attune-fcm-discrete-transect).

# References

Lee, S. & Fuhrman, J. A. (1987) Relationships between biovolume and
biomass of naturally derived marine bacterioplankton. Appl Env.
Microbiol 53: 1298--1303. Menden-Deuer, S. and Lessard, E.J. (2000)
Carbon to volume relationships for dinoflagellates, diatoms, and other
protist plankton. Limnology and Oceanography. 45(3): 569--579.
