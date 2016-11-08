<map><node BACKGROUND_COLOR="" COLOR="#000000" FOLDED="false" STYLE="fork" TEXT="seaice"><font BOLD="True" NAME="courier" SIZE="14" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Sea-ice realm specialization</dd><dt><b>ID</b></dt><dd>cmip6.seaice</dd><dt><b>QC status</b></dt><dd>draft</dd><dt><b>Contact</b></dt><dd>Ruth Petrie</dd><dt><b>Authors</b></dt><dd>Ruth Petrie, Bryan Lawrence, David Hassell</dd><dt><b>Contributors</b></dt><dd>Jamie Rae (UKMO)</dd>
    </dl>
  </body>
</html></richcontent><node POSITION="left" STYLE="bubble" TEXT="legend"><node BACKGROUND_COLOR="" COLOR="#000000" STYLE="bubble" TEXT="realm"><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Scientific area of a numerical model.</dd>
    </dl>
  </body>
</html></richcontent></node><node BACKGROUND_COLOR="#ccccff" COLOR="#000000" STYLE="bubble" TEXT="grid"><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Provides structure for description of a process simulated within a particular model realm.</dd>
    </dl>
  </body>
</html></richcontent></node><node BACKGROUND_COLOR="#ffff66" COLOR="#000000" STYLE="bubble" TEXT="key-properties"><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Provides structure for description of a process simulated within a particular model realm.</dd>
    </dl>
  </body>
</html></richcontent></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" STYLE="bubble" TEXT="process"><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Provides structure for description of a process simulated within a particular model realm.</dd>
    </dl>
  </body>
</html></richcontent></node><node BACKGROUND_COLOR="#ACF0F2" COLOR="#000000" STYLE="bubble" TEXT="sub-process"><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Provides structure for description of part of a process simulated within a particular model realm. Typically this will be a part of process which shares common properties.</dd>
    </dl>
  </body>
</html></richcontent></node><node BACKGROUND_COLOR="#F3FFE2" COLOR="#000000" STYLE="bubble" TEXT="detail"><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Provides details of specific properties of a process, sub-process, key properties, etc.  There are two possible specialisations expected: (1) A detail_vocabulary is identified, and a cardinality is assigned to that for possible responses; (2) Detail is used to provide a collection or a set of properties which are defined in the sub-class.</dd>
    </dl>
  </body>
</html></richcontent></node><node BACKGROUND_COLOR="#C9D787" COLOR="#000000" STYLE="bubble" TEXT="detail-property"><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>A property associated with a detail defined as a 4 member tuple: name, type, cardinality, description.</dd>
    </dl>
  </body>
</html></richcontent></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" STYLE="bubble" TEXT="enum-choice"><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>A choice within an enumeration.</dd>
    </dl>
  </body>
</html></richcontent></node></node><node BACKGROUND_COLOR="#ccccff" COLOR="#000000" FOLDED="false" STYLE="bubble" TEXT="grid"><font BOLD="True" NAME="courier" SIZE="12" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Sea ice grid and discretisation</dd><dt><b>ID</b></dt><dd>cmip6.seaice.grid</dd><dt><b>QC status</b></dt><dd>draft</dd><dt><b>Contact</b></dt><dd>Ruth Petrie</dd><dt><b>Authors</b></dt><dd>Ruth Petrie</dd>
    </dl>
  </body>
</html></richcontent><node BACKGROUND_COLOR="#ccccff" COLOR="#000000" FOLDED="false" STYLE="bubble" TEXT="discretisation"><font BOLD="True" NAME="courier" SIZE="12" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Types of sea ice discretisation</dd><dt><b>ID</b></dt><dd>cmip6.seaice.grid.discretisation</dd>
    </dl>
  </body>
</html></richcontent><node BACKGROUND_COLOR="#F3FFE2" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="horizontal"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>How the sea ice is horizontally discretised</dd><dt><b>ID</b></dt><dd>cmip6.seaice.grid.discretisation.horizontal</dd>
    </dl>
  </body>
</html></richcontent><node BACKGROUND_COLOR="#C9D787" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="horizontal"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Type of sea` ice horizontal discretisation</dd><dt><b>ID</b></dt><dd>cmip6.seaice.grid.discretisation.horizontal.horizontal</dd><dt><b>Type</b></dt><dd>enum</dd><dt><b>Cardinality</b></dt><dd>1.1</dd>
    </dl>
  </body>
</html></richcontent><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Type of sea` ice horizontal discretisation</dd><dt><b>ID</b></dt><dd>cmip6.seaice.grid.discretisation.horizontal.horizontal</dd><dt><b>Type</b></dt><dd>enum</dd><dt><b>Cardinality</b></dt><dd>1.1</dd>
    </dl>
  </body>
</html></richcontent><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Atmosphere Grid"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Sea ice is horizontally discretised on the atmospheric grid</dd><dt><b>ID</b></dt><dd>sea-ice-grid.atmosphere-grid</dd>
    </dl>
  </body>
</html></richcontent></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Ocean grid"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Sea ice is horizontally discretised on the ocean grid</dd><dt><b>ID</b></dt><dd>sea-ice-grid.ocean-grid</dd>
    </dl>
  </body>
</html></richcontent></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Own Grid"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Sea ice is horizontally discretised on it`s own independent grid</dd><dt><b>ID</b></dt><dd>sea-ice-grid.own-grid</dd>
    </dl>
  </body>
</html></richcontent></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Other"><font BOLD="True" NAME="courier" SIZE="10" /></node></node><node BACKGROUND_COLOR="#C9D787" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Additional grid details"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Specify any additional grid details</dd><dt><b>ID</b></dt><dd>cmip6.seaice.grid.discretisation.horizontal.Additional grid details</dd><dt><b>Type</b></dt><dd>str</dd><dt><b>Cardinality</b></dt><dd>0.1</dd>
    </dl>
  </body>
</html></richcontent><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Specify any additional grid details</dd><dt><b>ID</b></dt><dd>cmip6.seaice.grid.discretisation.horizontal.Additional grid details</dd><dt><b>Type</b></dt><dd>str</dd><dt><b>Cardinality</b></dt><dd>0.1</dd>
    </dl>
  </body>
</html></richcontent></node></node><node BACKGROUND_COLOR="#F3FFE2" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="layering"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Method used to represent sea ice layering</dd><dt><b>ID</b></dt><dd>cmip6.seaice.grid.discretisation.layering</dd>
    </dl>
  </body>
</html></richcontent><node BACKGROUND_COLOR="#C9D787" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="layering_type"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Type of sea` ice layering</dd><dt><b>ID</b></dt><dd>cmip6.seaice.grid.discretisation.layering.layering_type</dd><dt><b>Type</b></dt><dd>enum</dd><dt><b>Cardinality</b></dt><dd>1.N</dd>
    </dl>
  </body>
</html></richcontent><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Type of sea` ice layering</dd><dt><b>ID</b></dt><dd>cmip6.seaice.grid.discretisation.layering.layering_type</dd><dt><b>Type</b></dt><dd>enum</dd><dt><b>Cardinality</b></dt><dd>1.N</dd>
    </dl>
  </body>
</html></richcontent><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="2-levels"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Simulation uses two layers.</dd><dt><b>ID</b></dt><dd>layering-types.2-levels</dd>
    </dl>
  </body>
</html></richcontent></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Multi-level"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Simulation uses more than two layers</dd><dt><b>ID</b></dt><dd>layering-types.multi-level</dd>
    </dl>
  </body>
</html></richcontent></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="ice types"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Simulation does not use layers, but has multiple ice types per grid cell</dd><dt><b>ID</b></dt><dd>layering-types.ice-types</dd>
    </dl>
  </body>
</html></richcontent></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="snow layer"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Simulation has at least one snow layer</dd><dt><b>ID</b></dt><dd>layering-types.snow-layer</dd>
    </dl>
  </body>
</html></richcontent></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="zero-layer"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Simulation has no internal ice thermodynamics.</dd><dt><b>ID</b></dt><dd>layering-types.zero-layer</dd>
    </dl>
  </body>
</html></richcontent></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Other"><font BOLD="True" NAME="courier" SIZE="10" /></node></node></node><node BACKGROUND_COLOR="#F3FFE2" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Sea ice categories"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Method used to represent sea ice layering</dd><dt><b>ID</b></dt><dd>cmip6.seaice.grid.discretisation.Sea ice categories</dd>
    </dl>
  </body>
</html></richcontent><node BACKGROUND_COLOR="#C9D787" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Number of sea ice categories"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>If using multiple sea ice category specify how many</dd><dt><b>ID</b></dt><dd>cmip6.seaice.grid.discretisation.Sea ice categories.Number of sea ice categories</dd><dt><b>Type</b></dt><dd>str</dd><dt><b>Cardinality</b></dt><dd>0.1</dd>
    </dl>
  </body>
</html></richcontent><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>If using multiple sea ice category specify how many</dd><dt><b>ID</b></dt><dd>cmip6.seaice.grid.discretisation.Sea ice categories.Number of sea ice categories</dd><dt><b>Type</b></dt><dd>str</dd><dt><b>Cardinality</b></dt><dd>0.1</dd>
    </dl>
  </body>
</html></richcontent></node><node BACKGROUND_COLOR="#C9D787" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Sea ice category limits"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>If using multiple sea ice categories specify the category limits</dd><dt><b>ID</b></dt><dd>cmip6.seaice.grid.discretisation.Sea ice categories.Sea ice category limits</dd><dt><b>Type</b></dt><dd>str</dd><dt><b>Cardinality</b></dt><dd>0.1</dd>
    </dl>
  </body>
</html></richcontent><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>If using multiple sea ice categories specify the category limits</dd><dt><b>ID</b></dt><dd>cmip6.seaice.grid.discretisation.Sea ice categories.Sea ice category limits</dd><dt><b>Type</b></dt><dd>str</dd><dt><b>Cardinality</b></dt><dd>0.1</dd>
    </dl>
  </body>
</html></richcontent></node><node BACKGROUND_COLOR="#C9D787" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Sea ice thickness distribution scheme"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>If applicable describe the sea ice thickness distribution scheme</dd><dt><b>ID</b></dt><dd>cmip6.seaice.grid.discretisation.Sea ice categories.Sea ice thickness distribution scheme</dd><dt><b>Type</b></dt><dd>str</dd><dt><b>Cardinality</b></dt><dd>0.1</dd>
    </dl>
  </body>
</html></richcontent><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>If applicable describe the sea ice thickness distribution scheme</dd><dt><b>ID</b></dt><dd>cmip6.seaice.grid.discretisation.Sea ice categories.Sea ice thickness distribution scheme</dd><dt><b>Type</b></dt><dd>str</dd><dt><b>Cardinality</b></dt><dd>0.1</dd>
    </dl>
  </body>
</html></richcontent></node></node></node></node><node BACKGROUND_COLOR="#ffff66" COLOR="#000000" FOLDED="false" STYLE="bubble" TEXT="key_properties"><font BOLD="True" NAME="courier" SIZE="12" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Key properties of sea ice</dd><dt><b>ID</b></dt><dd>cmip6.seaice.key_properties</dd><dt><b>QC status</b></dt><dd>draft</dd><dt><b>Contact</b></dt><dd>Ruth Petrie</dd><dt><b>Authors</b></dt><dd>Ruth Petrie</dd>
    </dl>
  </body>
</html></richcontent><node BACKGROUND_COLOR="#F3FFE2" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="general"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>General key properties in sea ice</dd><dt><b>ID</b></dt><dd>cmip6.seaice.key_properties.general</dd>
    </dl>
  </body>
</html></richcontent><node BACKGROUND_COLOR="#C9D787" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="basic_approximations"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Basic approximations made in the ice.</dd><dt><b>ID</b></dt><dd>cmip6.seaice.key_properties.general.basic_approximations</dd><dt><b>Type</b></dt><dd>enum</dd><dt><b>Cardinality</b></dt><dd>1.N</dd>
    </dl>
  </body>
</html></richcontent><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Basic approximations made in the ice.</dd><dt><b>ID</b></dt><dd>cmip6.seaice.key_properties.general.basic_approximations</dd><dt><b>Type</b></dt><dd>enum</dd><dt><b>Cardinality</b></dt><dd>1.N</dd>
    </dl>
  </body>
</html></richcontent><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="EVP"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Elastic Viscous Plastic</dd><dt><b>ID</b></dt><dd>seaice-basic-approx-types.evp</dd>
    </dl>
  </body>
</html></richcontent></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Isotropic"><font BOLD="True" NAME="courier" SIZE="10" /></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Other"><font BOLD="True" NAME="courier" SIZE="10" /></node></node><node BACKGROUND_COLOR="#C9D787" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="prognostic_variables"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>List of prognostic variables in the sea ice component.</dd><dt><b>ID</b></dt><dd>cmip6.seaice.key_properties.general.prognostic_variables</dd><dt><b>Type</b></dt><dd>enum</dd><dt><b>Cardinality</b></dt><dd>1.N</dd>
    </dl>
  </body>
</html></richcontent><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>List of prognostic variables in the sea ice component.</dd><dt><b>ID</b></dt><dd>cmip6.seaice.key_properties.general.prognostic_variables</dd><dt><b>Type</b></dt><dd>enum</dd><dt><b>Cardinality</b></dt><dd>1.N</dd>
    </dl>
  </body>
</html></richcontent><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="list of prognostic variables"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Need to check on this</dd><dt><b>ID</b></dt><dd>prognostic-vars-types.list-of-prognostic-variables</dd>
    </dl>
  </body>
</html></richcontent></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Other"><font BOLD="True" NAME="courier" SIZE="10" /></node></node></node><node BACKGROUND_COLOR="#F3FFE2" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="seawater_properties"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Physical properties of seawater relevant to sea ice</dd><dt><b>ID</b></dt><dd>cmip6.seaice.key_properties.seawater_properties</dd>
    </dl>
  </body>
</html></richcontent><node BACKGROUND_COLOR="#C9D787" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="eos_type"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Type of EOS for sea water</dd><dt><b>ID</b></dt><dd>cmip6.seaice.key_properties.seawater_properties.eos_type</dd><dt><b>Type</b></dt><dd>enum</dd><dt><b>Cardinality</b></dt><dd>1.1</dd>
    </dl>
  </body>
</html></richcontent><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Type of EOS for sea water</dd><dt><b>ID</b></dt><dd>cmip6.seaice.key_properties.seawater_properties.eos_type</dd><dt><b>Type</b></dt><dd>enum</dd><dt><b>Cardinality</b></dt><dd>1.1</dd>
    </dl>
  </body>
</html></richcontent><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Jackett et al. 2006"><font BOLD="True" NAME="courier" SIZE="10" /></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Linear"><font BOLD="True" NAME="courier" SIZE="10" /></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Mc Dougall et al."><font BOLD="True" NAME="courier" SIZE="10" /></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="TEOS 2010"><font BOLD="True" NAME="courier" SIZE="10" /></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Other"><font BOLD="True" NAME="courier" SIZE="10" /></node></node><node BACKGROUND_COLOR="#C9D787" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="eos_functional_temp"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Temperature used in EOS for sea water</dd><dt><b>ID</b></dt><dd>cmip6.seaice.key_properties.seawater_properties.eos_functional_temp</dd><dt><b>Type</b></dt><dd>enum</dd><dt><b>Cardinality</b></dt><dd>1.1</dd>
    </dl>
  </body>
</html></richcontent><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Temperature used in EOS for sea water</dd><dt><b>ID</b></dt><dd>cmip6.seaice.key_properties.seawater_properties.eos_functional_temp</dd><dt><b>Type</b></dt><dd>enum</dd><dt><b>Cardinality</b></dt><dd>1.1</dd>
    </dl>
  </body>
</html></richcontent><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Conservative temperature"><font BOLD="True" NAME="courier" SIZE="10" /></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Potential temperature"><font BOLD="True" NAME="courier" SIZE="10" /></node></node><node BACKGROUND_COLOR="#C9D787" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="eos_functional_salt"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Salinity used in EOS for sea water</dd><dt><b>ID</b></dt><dd>cmip6.seaice.key_properties.seawater_properties.eos_functional_salt</dd><dt><b>Type</b></dt><dd>enum</dd><dt><b>Cardinality</b></dt><dd>1.1</dd>
    </dl>
  </body>
</html></richcontent><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Salinity used in EOS for sea water</dd><dt><b>ID</b></dt><dd>cmip6.seaice.key_properties.seawater_properties.eos_functional_salt</dd><dt><b>Type</b></dt><dd>enum</dd><dt><b>Cardinality</b></dt><dd>1.1</dd>
    </dl>
  </body>
</html></richcontent><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Absolute salinity Sa"><font BOLD="True" NAME="courier" SIZE="10" /></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Practical salinity Sp"><font BOLD="True" NAME="courier" SIZE="10" /></node></node><node BACKGROUND_COLOR="#C9D787" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="eos_functional_depth"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Depth or pressure used in EOS for sea water ?</dd><dt><b>ID</b></dt><dd>cmip6.seaice.key_properties.seawater_properties.eos_functional_depth</dd><dt><b>Type</b></dt><dd>enum</dd><dt><b>Cardinality</b></dt><dd>1.1</dd>
    </dl>
  </body>
</html></richcontent><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Depth or pressure used in EOS for sea water ?</dd><dt><b>ID</b></dt><dd>cmip6.seaice.key_properties.seawater_properties.eos_functional_depth</dd><dt><b>Type</b></dt><dd>enum</dd><dt><b>Cardinality</b></dt><dd>1.1</dd>
    </dl>
  </body>
</html></richcontent><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Depth (meters)"><font BOLD="True" NAME="courier" SIZE="10" /></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Pressure (dbars)"><font BOLD="True" NAME="courier" SIZE="10" /></node></node><node BACKGROUND_COLOR="#C9D787" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="ocean_freezing_point"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Equation used to compute the freezing point (in deg C) of seawater, as a function of salinity and pressure</dd><dt><b>ID</b></dt><dd>cmip6.seaice.key_properties.seawater_properties.ocean_freezing_point</dd><dt><b>Type</b></dt><dd>enum</dd><dt><b>Cardinality</b></dt><dd>1.1</dd>
    </dl>
  </body>
</html></richcontent><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Equation used to compute the freezing point (in deg C) of seawater, as a function of salinity and pressure</dd><dt><b>ID</b></dt><dd>cmip6.seaice.key_properties.seawater_properties.ocean_freezing_point</dd><dt><b>Type</b></dt><dd>enum</dd><dt><b>Cardinality</b></dt><dd>1.1</dd>
    </dl>
  </body>
</html></richcontent><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="TEOS 2010"><font BOLD="True" NAME="courier" SIZE="10" /></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Other"><font BOLD="True" NAME="courier" SIZE="10" /></node></node><node BACKGROUND_COLOR="#C9D787" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="ocean_specific_heat"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Specific heat in ocean (cpocean) in J/(kg K)</dd><dt><b>ID</b></dt><dd>cmip6.seaice.key_properties.seawater_properties.ocean_specific_heat</dd><dt><b>Type</b></dt><dd>float</dd><dt><b>Cardinality</b></dt><dd>1.1</dd>
    </dl>
  </body>
</html></richcontent><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Specific heat in ocean (cpocean) in J/(kg K)</dd><dt><b>ID</b></dt><dd>cmip6.seaice.key_properties.seawater_properties.ocean_specific_heat</dd><dt><b>Type</b></dt><dd>float</dd><dt><b>Cardinality</b></dt><dd>1.1</dd>
    </dl>
  </body>
</html></richcontent></node><node BACKGROUND_COLOR="#C9D787" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="ocean_reference_density"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Boussinesq reference density (rhozero) in kg / m3</dd><dt><b>ID</b></dt><dd>cmip6.seaice.key_properties.seawater_properties.ocean_reference_density</dd><dt><b>Type</b></dt><dd>float</dd><dt><b>Cardinality</b></dt><dd>1.1</dd>
    </dl>
  </body>
</html></richcontent><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Boussinesq reference density (rhozero) in kg / m3</dd><dt><b>ID</b></dt><dd>cmip6.seaice.key_properties.seawater_properties.ocean_reference_density</dd><dt><b>Type</b></dt><dd>float</dd><dt><b>Cardinality</b></dt><dd>1.1</dd>
    </dl>
  </body>
</html></richcontent></node></node><node BACKGROUND_COLOR="#ffff66" COLOR="#000000" FOLDED="false" STYLE="bubble" TEXT="conservation"><font BOLD="True" NAME="courier" SIZE="12" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Conservation in the sea ice component</dd><dt><b>ID</b></dt><dd>cmip6.seaice.key_properties.conservation</dd>
    </dl>
  </body>
</html></richcontent><node BACKGROUND_COLOR="#F3FFE2" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="details"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Extra properties of conservation in the sea ice component</dd><dt><b>ID</b></dt><dd>cmip6.seaice.key_properties.conservation.details</dd>
    </dl>
  </body>
</html></richcontent><node BACKGROUND_COLOR="#C9D787" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="scheme"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Properties conserved in sea ice by the numerical schemes</dd><dt><b>ID</b></dt><dd>cmip6.seaice.key_properties.conservation.details.scheme</dd><dt><b>Type</b></dt><dd>enum</dd><dt><b>Cardinality</b></dt><dd>1.N</dd>
    </dl>
  </body>
</html></richcontent><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Properties conserved in sea ice by the numerical schemes</dd><dt><b>ID</b></dt><dd>cmip6.seaice.key_properties.conservation.details.scheme</dd><dt><b>Type</b></dt><dd>enum</dd><dt><b>Cardinality</b></dt><dd>1.N</dd>
    </dl>
  </body>
</html></richcontent><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Energy"><font BOLD="True" NAME="courier" SIZE="10" /></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Freshwater"><font BOLD="True" NAME="courier" SIZE="10" /></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Mass"><font BOLD="True" NAME="courier" SIZE="10" /></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Salt"><font BOLD="True" NAME="courier" SIZE="10" /></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Other"><font BOLD="True" NAME="courier" SIZE="10" /></node></node><node BACKGROUND_COLOR="#C9D787" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="For each conserved property conserved please specify the terms which close the related budget"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>ID</b></dt><dd>cmip6.seaice.key_properties.conservation.details.For each conserved property conserved please specify the terms which close the related budget</dd><dt><b>Type</b></dt><dd>str</dd><dt><b>Cardinality</b></dt><dd>0.1</dd>
    </dl>
  </body>
</html></richcontent><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>ID</b></dt><dd>cmip6.seaice.key_properties.conservation.details.For each conserved property conserved please specify the terms which close the related budget</dd><dt><b>Type</b></dt><dd>str</dd><dt><b>Cardinality</b></dt><dd>0.1</dd>
    </dl>
  </body>
</html></richcontent></node><node BACKGROUND_COLOR="#C9D787" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="consistency_properties"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Any additional consistency properties (energy conversion, pressure gradient discretisation, ...)?</dd><dt><b>ID</b></dt><dd>cmip6.seaice.key_properties.conservation.details.consistency_properties</dd><dt><b>Type</b></dt><dd>str</dd><dt><b>Cardinality</b></dt><dd>0.1</dd>
    </dl>
  </body>
</html></richcontent><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Any additional consistency properties (energy conversion, pressure gradient discretisation, ...)?</dd><dt><b>ID</b></dt><dd>cmip6.seaice.key_properties.conservation.details.consistency_properties</dd><dt><b>Type</b></dt><dd>str</dd><dt><b>Cardinality</b></dt><dd>0.1</dd>
    </dl>
  </body>
</html></richcontent></node></node></node></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="false" STYLE="bubble" TEXT="dynamics"><font BOLD="True" NAME="courier" SIZE="12" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Characteristics of the Sea Ice Dynamics</dd><dt><b>ID</b></dt><dd>cmip6.seaice.dynamics</dd><dt><b>QC status</b></dt><dd>draft</dd><dt><b>Contact</b></dt><dd>Ruth Petrie</dd><dt><b>Authors</b></dt><dd>Ruth Petrie, Bryan Lawrence</dd>
    </dl>
  </body>
</html></richcontent><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Characteristics of the Sea Ice Dynamics</dd><dt><b>ID</b></dt><dd>cmip6.seaice.dynamics</dd><dt><b>QC status</b></dt><dd>draft</dd><dt><b>Contact</b></dt><dd>Ruth Petrie</dd><dt><b>Authors</b></dt><dd>Ruth Petrie, Bryan Lawrence</dd>
    </dl>
  </body>
</html></richcontent><node BACKGROUND_COLOR="#ACF0F2" COLOR="#000000" FOLDED="false" STYLE="bubble" TEXT="horizontal_advection"><font BOLD="True" NAME="courier" SIZE="12" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Method of horizontal advection</dd><dt><b>ID</b></dt><dd>cmip6.seaice.dynamics.horizontal_advection</dd>
    </dl>
  </body>
</html></richcontent><node BACKGROUND_COLOR="#F3FFE2" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="transport_method"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Horizontal advection of sea ice</dd><dt><b>ID</b></dt><dd>cmip6.seaice.dynamics.horizontal_advection.transport_method</dd>
    </dl>
  </body>
</html></richcontent><node BACKGROUND_COLOR="#C9D787" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="transport_method"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Method of horizontal advection</dd><dt><b>ID</b></dt><dd>cmip6.seaice.dynamics.horizontal_advection.transport_method.transport_method</dd><dt><b>Type</b></dt><dd>enum</dd><dt><b>Cardinality</b></dt><dd>0.1</dd>
    </dl>
  </body>
</html></richcontent><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Method of horizontal advection</dd><dt><b>ID</b></dt><dd>cmip6.seaice.dynamics.horizontal_advection.transport_method.transport_method</dd><dt><b>Type</b></dt><dd>enum</dd><dt><b>Cardinality</b></dt><dd>0.1</dd>
    </dl>
  </body>
</html></richcontent><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Eulerian"><font BOLD="True" NAME="courier" SIZE="10" /></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Incremental Re-mapping"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>(including Semi-Lagrangian)</dd><dt><b>ID</b></dt><dd>transport-methods.incremental-re-mapping</dd>
    </dl>
  </body>
</html></richcontent></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Prather"><font BOLD="True" NAME="courier" SIZE="10" /></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Other"><font BOLD="True" NAME="courier" SIZE="10" /></node></node></node></node><node BACKGROUND_COLOR="#ACF0F2" COLOR="#000000" FOLDED="false" STYLE="bubble" TEXT="transport_in_thickness_space"><font BOLD="True" NAME="courier" SIZE="12" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Method of ice migration in thickness</dd><dt><b>ID</b></dt><dd>cmip6.seaice.dynamics.transport_in_thickness_space</dd>
    </dl>
  </body>
</html></richcontent><node BACKGROUND_COLOR="#F3FFE2" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="transport_method"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Method of migration of sea ice in thickness</dd><dt><b>ID</b></dt><dd>cmip6.seaice.dynamics.transport_in_thickness_space.transport_method</dd>
    </dl>
  </body>
</html></richcontent><node BACKGROUND_COLOR="#C9D787" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="transport_method"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Method of ice migration in thickness</dd><dt><b>ID</b></dt><dd>cmip6.seaice.dynamics.transport_in_thickness_space.transport_method.transport_method</dd><dt><b>Type</b></dt><dd>enum</dd><dt><b>Cardinality</b></dt><dd>0.1</dd>
    </dl>
  </body>
</html></richcontent><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Method of ice migration in thickness</dd><dt><b>ID</b></dt><dd>cmip6.seaice.dynamics.transport_in_thickness_space.transport_method.transport_method</dd><dt><b>Type</b></dt><dd>enum</dd><dt><b>Cardinality</b></dt><dd>0.1</dd>
    </dl>
  </body>
</html></richcontent><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Eulerian"><font BOLD="True" NAME="courier" SIZE="10" /></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Incremental Re-mapping"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>(including Semi-Lagrangian)</dd><dt><b>ID</b></dt><dd>transport-methods.incremental-re-mapping</dd>
    </dl>
  </body>
</html></richcontent></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Prather"><font BOLD="True" NAME="courier" SIZE="10" /></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Other"><font BOLD="True" NAME="courier" SIZE="10" /></node></node></node></node><node BACKGROUND_COLOR="#ACF0F2" COLOR="#000000" FOLDED="false" STYLE="bubble" TEXT="redistribution"><font BOLD="True" NAME="courier" SIZE="12" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Sea Ice Mechanical Redistribution</dd><dt><b>ID</b></dt><dd>cmip6.seaice.dynamics.redistribution</dd>
    </dl>
  </body>
</html></richcontent><node BACKGROUND_COLOR="#F3FFE2" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="ice_redistribution"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Methods of mechanical redistribution of sea ice</dd><dt><b>ID</b></dt><dd>cmip6.seaice.dynamics.redistribution.ice_redistribution</dd>
    </dl>
  </body>
</html></richcontent><node BACKGROUND_COLOR="#C9D787" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="processes"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Additional processes which can redistribute sea ice.</dd><dt><b>ID</b></dt><dd>cmip6.seaice.dynamics.redistribution.ice_redistribution.processes</dd><dt><b>Type</b></dt><dd>enum</dd><dt><b>Cardinality</b></dt><dd>0.N</dd>
    </dl>
  </body>
</html></richcontent><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Additional processes which can redistribute sea ice.</dd><dt><b>ID</b></dt><dd>cmip6.seaice.dynamics.redistribution.ice_redistribution.processes</dd><dt><b>Type</b></dt><dd>enum</dd><dt><b>Cardinality</b></dt><dd>0.N</dd>
    </dl>
  </body>
</html></richcontent><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Rafting"><font BOLD="True" NAME="courier" SIZE="10" /></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Ridging"><font BOLD="True" NAME="courier" SIZE="10" /></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Other"><font BOLD="True" NAME="courier" SIZE="10" /></node></node><node BACKGROUND_COLOR="#C9D787" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="ice_strength_formulation"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Describe how ice-strength is formulated</dd><dt><b>ID</b></dt><dd>cmip6.seaice.dynamics.redistribution.ice_redistribution.ice_strength_formulation</dd><dt><b>Type</b></dt><dd>str</dd><dt><b>Cardinality</b></dt><dd>0.1</dd>
    </dl>
  </body>
</html></richcontent><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Describe how ice-strength is formulated</dd><dt><b>ID</b></dt><dd>cmip6.seaice.dynamics.redistribution.ice_redistribution.ice_strength_formulation</dd><dt><b>Type</b></dt><dd>str</dd><dt><b>Cardinality</b></dt><dd>0.1</dd>
    </dl>
  </body>
</html></richcontent></node></node></node><node BACKGROUND_COLOR="#ACF0F2" COLOR="#000000" FOLDED="false" STYLE="bubble" TEXT="rheology"><font BOLD="True" NAME="courier" SIZE="12" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Sea ice deformation</dd><dt><b>ID</b></dt><dd>cmip6.seaice.dynamics.rheology</dd>
    </dl>
  </body>
</html></richcontent><node BACKGROUND_COLOR="#F3FFE2" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="ice_deformation_method"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Methods of sea ice deformation</dd><dt><b>ID</b></dt><dd>cmip6.seaice.dynamics.rheology.ice_deformation_method</dd>
    </dl>
  </body>
</html></richcontent><node BACKGROUND_COLOR="#C9D787" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="ice_deformation_method"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Ice deformation method</dd><dt><b>ID</b></dt><dd>cmip6.seaice.dynamics.rheology.ice_deformation_method.ice_deformation_method</dd><dt><b>Type</b></dt><dd>enum</dd><dt><b>Cardinality</b></dt><dd>1.1</dd>
    </dl>
  </body>
</html></richcontent><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Ice deformation method</dd><dt><b>ID</b></dt><dd>cmip6.seaice.dynamics.rheology.ice_deformation_method.ice_deformation_method</dd><dt><b>Type</b></dt><dd>enum</dd><dt><b>Cardinality</b></dt><dd>1.1</dd>
    </dl>
  </body>
</html></richcontent><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Mohr-Coloumb"><font BOLD="True" NAME="courier" SIZE="10" /></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="elastic-visco-plastic"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>EVP</dd><dt><b>ID</b></dt><dd>rheology-types.elastic-visco-plastic</dd>
    </dl>
  </body>
</html></richcontent></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="free-drift"><font BOLD="True" NAME="courier" SIZE="10" /></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="granular"><font BOLD="True" NAME="courier" SIZE="10" /></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="other"><font BOLD="True" NAME="courier" SIZE="10" /></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="visco-plastic"><font BOLD="True" NAME="courier" SIZE="10" /></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Other"><font BOLD="True" NAME="courier" SIZE="10" /></node></node></node></node></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="false" STYLE="bubble" TEXT="thermodynamics"><font BOLD="True" NAME="courier" SIZE="12" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Characteristics of sea ice thermodynamics processes</dd><dt><b>ID</b></dt><dd>cmip6.seaice.thermodynamics</dd><dt><b>QC status</b></dt><dd>draft</dd><dt><b>Contact</b></dt><dd>Ruth Petrie</dd><dt><b>Authors</b></dt><dd>Ruth Petrie, Bryan Lawrence</dd>
    </dl>
  </body>
</html></richcontent><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Characteristics of sea ice thermodynamics processes</dd><dt><b>ID</b></dt><dd>cmip6.seaice.thermodynamics</dd><dt><b>QC status</b></dt><dd>draft</dd><dt><b>Contact</b></dt><dd>Ruth Petrie</dd><dt><b>Authors</b></dt><dd>Ruth Petrie, Bryan Lawrence</dd>
    </dl>
  </body>
</html></richcontent><node BACKGROUND_COLOR="#ACF0F2" COLOR="#000000" FOLDED="false" STYLE="bubble" TEXT="thermo_processes"><font BOLD="True" NAME="courier" SIZE="12" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Information about basal heat flux and brine inclusions</dd><dt><b>ID</b></dt><dd>cmip6.seaice.thermodynamics.thermo_processes</dd>
    </dl>
  </body>
</html></richcontent><node BACKGROUND_COLOR="#F3FFE2" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="details"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Information about basal heat flux and brine inclusions</dd><dt><b>ID</b></dt><dd>cmip6.seaice.thermodynamics.thermo_processes.details</dd>
    </dl>
  </body>
</html></richcontent><node BACKGROUND_COLOR="#C9D787" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="brine_inclusion_method"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Method by which basal heat flux is handled</dd><dt><b>ID</b></dt><dd>cmip6.seaice.thermodynamics.thermo_processes.details.brine_inclusion_method</dd><dt><b>Type</b></dt><dd>enum</dd><dt><b>Cardinality</b></dt><dd>0.1</dd>
    </dl>
  </body>
</html></richcontent><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Method by which basal heat flux is handled</dd><dt><b>ID</b></dt><dd>cmip6.seaice.thermodynamics.thermo_processes.details.brine_inclusion_method</dd><dt><b>Type</b></dt><dd>enum</dd><dt><b>Cardinality</b></dt><dd>0.1</dd>
    </dl>
  </body>
</html></richcontent><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Heat Reservoir"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Brine inclusions treated as a heat reservoir</dd><dt><b>ID</b></dt><dd>thermo-brine-types.heat-reservoir</dd>
    </dl>
  </body>
</html></richcontent></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="None"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>No brine inclusions included in sea ice thermodynamics</dd><dt><b>ID</b></dt><dd>thermo-brine-types.none</dd>
    </dl>
  </body>
</html></richcontent></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Thermal Fixed Salinity"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Thermal properties depend on S-T (with fixed salinity)</dd><dt><b>ID</b></dt><dd>thermo-brine-types.thermal-fixed-salinity</dd>
    </dl>
  </body>
</html></richcontent></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Thermal Varying Salinity"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Thermal properties depend on S-T (with varying salinity</dd><dt><b>ID</b></dt><dd>thermo-brine-types.thermal-varying-salinity</dd>
    </dl>
  </body>
</html></richcontent></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Other"><font BOLD="True" NAME="courier" SIZE="10" /></node></node><node BACKGROUND_COLOR="#C9D787" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="fixed_salinity_value"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>If you have selected "Thermal properties depend on S-T (with fixed salinity)" please supply the salinity value used.</dd><dt><b>ID</b></dt><dd>cmip6.seaice.thermodynamics.thermo_processes.details.fixed_salinity_value</dd><dt><b>Type</b></dt><dd>float</dd><dt><b>Cardinality</b></dt><dd>0.1</dd>
    </dl>
  </body>
</html></richcontent><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>If you have selected "Thermal properties depend on S-T (with fixed salinity)" please supply the salinity value used.</dd><dt><b>ID</b></dt><dd>cmip6.seaice.thermodynamics.thermo_processes.details.fixed_salinity_value</dd><dt><b>Type</b></dt><dd>float</dd><dt><b>Cardinality</b></dt><dd>0.1</dd>
    </dl>
  </body>
</html></richcontent></node><node BACKGROUND_COLOR="#C9D787" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="basal_heat_flux"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Method by which basal heat flux is handled</dd><dt><b>ID</b></dt><dd>cmip6.seaice.thermodynamics.thermo_processes.details.basal_heat_flux</dd><dt><b>Type</b></dt><dd>str</dd><dt><b>Cardinality</b></dt><dd>0.1</dd>
    </dl>
  </body>
</html></richcontent><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Method by which basal heat flux is handled</dd><dt><b>ID</b></dt><dd>cmip6.seaice.thermodynamics.thermo_processes.details.basal_heat_flux</dd><dt><b>Type</b></dt><dd>str</dd><dt><b>Cardinality</b></dt><dd>0.1</dd>
    </dl>
  </body>
</html></richcontent></node><node BACKGROUND_COLOR="#C9D787" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="brine_inclusions"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Method by which brine inclusions are handled</dd><dt><b>ID</b></dt><dd>cmip6.seaice.thermodynamics.thermo_processes.details.brine_inclusions</dd><dt><b>Type</b></dt><dd>str</dd><dt><b>Cardinality</b></dt><dd>0.1</dd>
    </dl>
  </body>
</html></richcontent><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Method by which brine inclusions are handled</dd><dt><b>ID</b></dt><dd>cmip6.seaice.thermodynamics.thermo_processes.details.brine_inclusions</dd><dt><b>Type</b></dt><dd>str</dd><dt><b>Cardinality</b></dt><dd>0.1</dd>
    </dl>
  </body>
</html></richcontent></node></node></node><node BACKGROUND_COLOR="#ACF0F2" COLOR="#000000" FOLDED="false" STYLE="bubble" TEXT="snow_processes"><font BOLD="True" NAME="courier" SIZE="12" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Snow processes in sea ice thermodynamics</dd><dt><b>ID</b></dt><dd>cmip6.seaice.thermodynamics.snow_processes</dd>
    </dl>
  </body>
</html></richcontent><node BACKGROUND_COLOR="#F3FFE2" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="process_type"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Snow on ice processes</dd><dt><b>ID</b></dt><dd>cmip6.seaice.thermodynamics.snow_processes.process_type</dd>
    </dl>
  </body>
</html></richcontent><node BACKGROUND_COLOR="#C9D787" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="process_type"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Snow processes in sea ice thermodynamics</dd><dt><b>ID</b></dt><dd>cmip6.seaice.thermodynamics.snow_processes.process_type.process_type</dd><dt><b>Type</b></dt><dd>enum</dd><dt><b>Cardinality</b></dt><dd>1.N</dd>
    </dl>
  </body>
</html></richcontent><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Snow processes in sea ice thermodynamics</dd><dt><b>ID</b></dt><dd>cmip6.seaice.thermodynamics.snow_processes.process_type.process_type</dd><dt><b>Type</b></dt><dd>enum</dd><dt><b>Cardinality</b></dt><dd>1.N</dd>
    </dl>
  </body>
</html></richcontent><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="multi-layered heat diffusion"><font BOLD="True" NAME="courier" SIZE="10" /></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="single-layered heat diffusion"><font BOLD="True" NAME="courier" SIZE="10" /></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="snow aging scheme"><font BOLD="True" NAME="courier" SIZE="10" /></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="snow ice scheme"><font BOLD="True" NAME="courier" SIZE="10" /></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="snow redistribution scheme"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Is there a scheme to redistribute snow on sea ice by wind or melting processes?</dd><dt><b>ID</b></dt><dd>snow-process-types.snow-redistribution-scheme</dd>
    </dl>
  </body>
</html></richcontent></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Other"><font BOLD="True" NAME="courier" SIZE="10" /></node></node><node BACKGROUND_COLOR="#C9D787" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="heat_content_precip"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Method by which the heat content of precipitation is handled</dd><dt><b>ID</b></dt><dd>cmip6.seaice.thermodynamics.snow_processes.process_type.heat_content_precip</dd><dt><b>Type</b></dt><dd>str</dd><dt><b>Cardinality</b></dt><dd>0.1</dd>
    </dl>
  </body>
</html></richcontent><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Method by which the heat content of precipitation is handled</dd><dt><b>ID</b></dt><dd>cmip6.seaice.thermodynamics.snow_processes.process_type.heat_content_precip</dd><dt><b>Type</b></dt><dd>str</dd><dt><b>Cardinality</b></dt><dd>0.1</dd>
    </dl>
  </body>
</html></richcontent></node></node></node><node BACKGROUND_COLOR="#ACF0F2" COLOR="#000000" FOLDED="false" STYLE="bubble" TEXT="vertical_heat_diffusion"><font BOLD="True" NAME="courier" SIZE="12" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Characteristics of vertical heat diffusion in sea ice.</dd><dt><b>ID</b></dt><dd>cmip6.seaice.thermodynamics.vertical_heat_diffusion</dd>
    </dl>
  </body>
</html></richcontent><node BACKGROUND_COLOR="#F3FFE2" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="details"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Characteristics of vertical heat diffusion in sea ice.</dd><dt><b>ID</b></dt><dd>cmip6.seaice.thermodynamics.vertical_heat_diffusion.details</dd>
    </dl>
  </body>
</html></richcontent><node BACKGROUND_COLOR="#C9D787" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="num_of_layers"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Number of layers used for vertical heat diffusion</dd><dt><b>ID</b></dt><dd>cmip6.seaice.thermodynamics.vertical_heat_diffusion.details.num_of_layers</dd><dt><b>Type</b></dt><dd>int</dd><dt><b>Cardinality</b></dt><dd>1.1</dd>
    </dl>
  </body>
</html></richcontent><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Number of layers used for vertical heat diffusion</dd><dt><b>ID</b></dt><dd>cmip6.seaice.thermodynamics.vertical_heat_diffusion.details.num_of_layers</dd><dt><b>Type</b></dt><dd>int</dd><dt><b>Cardinality</b></dt><dd>1.1</dd>
    </dl>
  </body>
</html></richcontent></node><node BACKGROUND_COLOR="#C9D787" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="regular_grid"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>If multiple layers, are they regularly distributed?</dd><dt><b>ID</b></dt><dd>cmip6.seaice.thermodynamics.vertical_heat_diffusion.details.regular_grid</dd><dt><b>Type</b></dt><dd>bool</dd><dt><b>Cardinality</b></dt><dd>0.1</dd>
    </dl>
  </body>
</html></richcontent><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>If multiple layers, are they regularly distributed?</dd><dt><b>ID</b></dt><dd>cmip6.seaice.thermodynamics.vertical_heat_diffusion.details.regular_grid</dd><dt><b>Type</b></dt><dd>bool</dd><dt><b>Cardinality</b></dt><dd>0.1</dd>
    </dl>
  </body>
</html></richcontent></node><node BACKGROUND_COLOR="#C9D787" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="based_on_semtner"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Is method based on Semtner 1976?</dd><dt><b>ID</b></dt><dd>cmip6.seaice.thermodynamics.vertical_heat_diffusion.details.based_on_semtner</dd><dt><b>Type</b></dt><dd>bool</dd><dt><b>Cardinality</b></dt><dd>1.1</dd>
    </dl>
  </body>
</html></richcontent><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Is method based on Semtner 1976?</dd><dt><b>ID</b></dt><dd>cmip6.seaice.thermodynamics.vertical_heat_diffusion.details.based_on_semtner</dd><dt><b>Type</b></dt><dd>bool</dd><dt><b>Cardinality</b></dt><dd>1.1</dd>
    </dl>
  </body>
</html></richcontent></node></node></node><node BACKGROUND_COLOR="#ACF0F2" COLOR="#000000" FOLDED="false" STYLE="bubble" TEXT="additional_processes"><font BOLD="True" NAME="courier" SIZE="12" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Additonal processes not elsewhere described</dd><dt><b>ID</b></dt><dd>cmip6.seaice.thermodynamics.additional_processes</dd>
    </dl>
  </body>
</html></richcontent><node BACKGROUND_COLOR="#F3FFE2" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="details"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Additonal processes not elsewhere described</dd><dt><b>ID</b></dt><dd>cmip6.seaice.thermodynamics.additional_processes.details</dd>
    </dl>
  </body>
</html></richcontent><node BACKGROUND_COLOR="#C9D787" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="processes"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Additional processes</dd><dt><b>ID</b></dt><dd>cmip6.seaice.thermodynamics.additional_processes.details.processes</dd><dt><b>Type</b></dt><dd>enum</dd><dt><b>Cardinality</b></dt><dd>0.N</dd>
    </dl>
  </body>
</html></richcontent><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Additional processes</dd><dt><b>ID</b></dt><dd>cmip6.seaice.thermodynamics.additional_processes.details.processes</dd><dt><b>Type</b></dt><dd>enum</dd><dt><b>Cardinality</b></dt><dd>0.N</dd>
    </dl>
  </body>
</html></richcontent><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Biogeochemistry"><font BOLD="True" NAME="courier" SIZE="10" /></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Chemistry"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>e.g. black carbon</dd><dt><b>ID</b></dt><dd>add-processes.chemistry</dd>
    </dl>
  </body>
</html></richcontent></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Frazil ice"><font BOLD="True" NAME="courier" SIZE="10" /></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Ice lateral melting"><font BOLD="True" NAME="courier" SIZE="10" /></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Ice radiation transmission"><font BOLD="True" NAME="courier" SIZE="10" /></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Ice surface sublimation"><font BOLD="True" NAME="courier" SIZE="10" /></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Melt ponds"><font BOLD="True" NAME="courier" SIZE="10" /></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="New ice formation"><font BOLD="True" NAME="courier" SIZE="10" /></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="Other"><font BOLD="True" NAME="courier" SIZE="10" /></node></node></node></node></node><node BACKGROUND_COLOR="#FFFFFF" COLOR="#000000" FOLDED="false" STYLE="bubble" TEXT="radiative_processes"><font BOLD="True" NAME="courier" SIZE="12" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Radiative processes in sea ice</dd><dt><b>ID</b></dt><dd>cmip6.seaice.radiative_processes</dd><dt><b>QC status</b></dt><dd>draft</dd><dt><b>Contact</b></dt><dd>Ruth Petrie</dd><dt><b>Authors</b></dt><dd>Ruth Petrie, Bryan Lawrence</dd>
    </dl>
  </body>
</html></richcontent><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Radiative processes in sea ice</dd><dt><b>ID</b></dt><dd>cmip6.seaice.radiative_processes</dd><dt><b>QC status</b></dt><dd>draft</dd><dt><b>Contact</b></dt><dd>Ruth Petrie</dd><dt><b>Authors</b></dt><dd>Ruth Petrie, Bryan Lawrence</dd>
    </dl>
  </body>
</html></richcontent><node BACKGROUND_COLOR="#ACF0F2" COLOR="#000000" FOLDED="false" STYLE="bubble" TEXT="si_radiative_process_methods"><font BOLD="True" NAME="courier" SIZE="12" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Properties of radiation in sea ice thermodynamics</dd><dt><b>ID</b></dt><dd>cmip6.seaice.radiative_processes.si_radiative_process_methods</dd>
    </dl>
  </body>
</html></richcontent><node BACKGROUND_COLOR="#F3FFE2" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="details"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Additional information about radiative processes in sea ice.</dd><dt><b>ID</b></dt><dd>cmip6.seaice.radiative_processes.si_radiative_process_methods.details</dd>
    </dl>
  </body>
</html></richcontent><node BACKGROUND_COLOR="#C9D787" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="surface_albedo"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Method used to handle surface albedo</dd><dt><b>ID</b></dt><dd>cmip6.seaice.radiative_processes.si_radiative_process_methods.details.surface_albedo</dd><dt><b>Type</b></dt><dd>str</dd><dt><b>Cardinality</b></dt><dd>0.1</dd>
    </dl>
  </body>
</html></richcontent><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Method used to handle surface albedo</dd><dt><b>ID</b></dt><dd>cmip6.seaice.radiative_processes.si_radiative_process_methods.details.surface_albedo</dd><dt><b>Type</b></dt><dd>str</dd><dt><b>Cardinality</b></dt><dd>0.1</dd>
    </dl>
  </body>
</html></richcontent></node><node BACKGROUND_COLOR="#C9D787" COLOR="#000000" FOLDED="true" STYLE="bubble" TEXT="ice_radiation_transmission"><font BOLD="True" NAME="courier" SIZE="10" /><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Method by which solar radiation through sea ice is handled</dd><dt><b>ID</b></dt><dd>cmip6.seaice.radiative_processes.si_radiative_process_methods.details.ice_radiation_transmission</dd><dt><b>Type</b></dt><dd>str</dd><dt><b>Cardinality</b></dt><dd>0.1</dd>
    </dl>
  </body>
</html></richcontent><richcontent TYPE="NOTE"><html>
  <head />
  <body>
    <dl>
        <dt><b>Description</b></dt><dd>Method by which solar radiation through sea ice is handled</dd><dt><b>ID</b></dt><dd>cmip6.seaice.radiative_processes.si_radiative_process_methods.details.ice_radiation_transmission</dd><dt><b>Type</b></dt><dd>str</dd><dt><b>Cardinality</b></dt><dd>0.1</dd>
    </dl>
  </body>
</html></richcontent></node></node></node></node></node></map>