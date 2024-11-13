

head='''<?xml version="1.0"?>
<chroma>
<Param>
  <InlineMeasurements>

'''

tail='''
  </InlineMeasurements>
   <nrow>%(NL)s %(NL)s %(NL)s %(NT)s</nrow>
</Param>

<Cfg>
 <cfg_type>WEAK_FIELD</cfg_type>
 <cfg_file>dummy</cfg_file>
  <parallel_io>true</parallel_io>
</Cfg>
</chroma>
'''

wflow_cfg = """<elem>
<Name>WILSON_FLOW</Name>
<Frequency>1</Frequency>
<Param>
  <version>1</version>
  <nstep>%(FLOW_STEP)s</nstep>
  <wtime>%(FLOW_TIME)s</wtime>
  <t_dir>-1</t_dir>
</Param>
<NamedObject>
  <gauge_in>%(CFG_PREFLOW)s</gauge_in>
  <gauge_out>%(CFG_FLOW)s</gauge_out>
</NamedObject>
</elem>

"""

qio_read='''<elem>
<Name>QIO_READ_NAMED_OBJECT</Name>
<Frequency>1</Frequency>
<NamedObject>
  <object_id>%(OBJ_ID)s</object_id>
  <object_type>%(OBJ_TYPE)s</object_type>
</NamedObject>
<File>
  <file_name>%(LIME_FILE)s</file_name>
  <file_volfmt>SINGLEFILE</file_volfmt>
  <parallel_io>true</parallel_io>
</File>
</elem>

'''

qio_erase='''<elem>
<Name>ERASE_NAMED_OBJECT</Name>
<Frequency>1</Frequency>
<NamedObject>
  <object_id>%(OBJ_ID)s</object_id>
</NamedObject>
</elem>

'''

qio_write='''<elem>
<Name>QIO_WRITE_NAMED_OBJECT</Name>
<Frequency>1</Frequency>
<NamedObject>
  <object_id>%(OBJ_ID)s</object_id>
  <object_type>%(OBJ_TYPE)s</object_type>
</NamedObject>
<File>
  <file_name>%(LIME_FILE)s</file_name>
  <file_volfmt>SINGLEFILE</file_volfmt>
  <parallel_io>true</parallel_io>
</File>
</elem>

'''

qio_write_erase='''<elem>
<Name>QIO_WRITE_ERASE_NAMED_OBJECT</Name>
<Frequency>1</Frequency>
<NamedObject>
  <object_id>%(OBJ_ID)s</object_id>
  <object_type>%(OBJ_TYPE)s</object_type>
</NamedObject>
<File>
  <file_name>%(LIME_FILE)s</file_name>
  <file_volfmt>SINGLEFILE</file_volfmt>
  <parallel_io>true</parallel_io>
</File>
</elem>

'''

shell_source='''<elem>
<Name>MAKE_SOURCE</Name>
<Frequency>1</Frequency>
<Param>
<version>6</version>
<Source>
    <version>1</version>
    <SourceType>SHELL_SOURCE</SourceType>
    <j_decay>3</j_decay>
    <t_srce>%(X)s %(Y)s %(Z)s %(T)s</t_srce>
    <SmearingParam>
        <wvf_kind>GAUGE_INV_GAUSSIAN</wvf_kind>
        <wvf_param>2.0</wvf_param>
        <wvfIntPar>5</wvfIntPar>
        <no_smear_dir>3</no_smear_dir>
    </SmearingParam>
</Source>
</Param>
<NamedObject>
  <gauge_id>default_gauge_field</gauge_id>
  <source_id>%(SRC_NAME)s</source_id>
</NamedObject>
</elem>

'''

prop_test='''<elem>
<Name>PROPAGATOR</Name>
<Frequency>1</Frequency>
      <Param>
        <version>10</version>
        <quarkSpinType>FULL</quarkSpinType>
        <obsvP>true</obsvP>
        <numRetries>1</numRetries>
        <FermionAction>
         <FermAct>WILSON</FermAct>
         <Kappa>0.11</Kappa>
         <AnisoParam>
           <anisoP>false</anisoP>
           <t_dir>3</t_dir>
           <xi_0>1.0</xi_0>
           <nu>1.0</nu>
         </AnisoParam>
         <FermionBC>
           <FermBC>SIMPLE_FERMBC</FermBC>
           <boundary>1 1 1 -1</boundary>
         </FermionBC>
        </FermionAction>
<InvertParam>
  <invType>CG_INVERTER</invType>
  <RsdCG>1e-5</RsdCG>
  <MaxCG>1200</MaxCG>
</InvertParam>
      </Param>
<NamedObject>
  <gauge_id>default_gauge_field</gauge_id>
  <source_id>%(SRC_NAME)s</source_id>
  <prop_id>%(PROP_NAME)s</prop_id>
</NamedObject>
<xml_file>%(PROP_NAME)s.out.xml</xml_file>
</elem>

'''

hadron_spectrum='''
     <elem>
      <annotation>
         Compute the hadron spectrum.
         This version is a clone of the one below, however the xml output is
         written within the same chroma output file
      </annotation>
      <Name>HADRON_SPECTRUM</Name>
      <Frequency>1</Frequency>
      <Param>
        <version>1</version>
        <MesonP>false</MesonP>
        <CurrentP>true</CurrentP>
        <BaryonP>false</BaryonP>
        <time_rev>false</time_rev>
        <mom2_max>3</mom2_max>
        <avg_equiv_mom>true</avg_equiv_mom>
       </Param>
      <NamedObject>
        <gauge_id>default_gauge_field</gauge_id>
        <sink_pairs>
          <elem>
            <first_id>%(UP_QUARK)s</first_id>
            <second_id>%(DN_QUARK)s</second_id>
          </elem>
          <elem>
            <first_id>%(UP_QUARK)s</first_id>
            <second_id>%(STRANGE_QUARK)s</second_id>
          </elem>
        </sink_pairs>
      </NamedObject>  
    </elem>

'''


shell_sink='''
<elem>
<Name>SINK_SMEAR</Name>
<Frequency>1</Frequency>
<Param>
<version>5</version>
<Sink>
  <version>2</version>
  <SinkType>SHELL_SINK</SinkType>
  <j_decay>3</j_decay>
  <SmearingParam>
    <wvf_kind>GAUGE_INV_GAUSSIAN</wvf_kind>
    <wvf_param>2.0</wvf_param>
    <wvfIntPar>5</wvfIntPar>
    <no_smear_dir>3</no_smear_dir>
  </SmearingParam>
</Sink>
</Param>
<NamedObject>
  <gauge_id>default_gauge_field</gauge_id>
  <prop_id>%(PROP_NAME)s</prop_id>
  <smeared_prop_id>%(SMEARED_PROP)s</smeared_prop_id>
</NamedObject>
</elem>

'''

mres_iso='''<elem>
<Name>MESON_CONTRACTIONS</Name>
<MesonParams>
<p2_max>0</p2_max>
<particle_list>
  <elem>piplus</elem>
</particle_list>
<h5_file_name>%(MRES_FILE)s</h5_file_name>
<obj_path>/pseudo_pseudo_UD</obj_path>
</MesonParams>
  <NamedObject>
    <up_quark>%(UP_QUARK)s</up_quark>
    <down_quark>%(DN_QUARK)s</down_quark>
  </NamedObject>
</elem>

<elem>
<Name>MESON_CONTRACTIONS</Name>
<MesonParams>
<p2_max>0</p2_max>
<particle_list>
  <elem>piplus</elem>
</particle_list>
<h5_file_name>%(MRES_FILE)s</h5_file_name>
<obj_path>/midpoint_pseudo_UD</obj_path>
</MesonParams>
  <NamedObject>
    <up_quark>%(UP_QUARK)s_MP</up_quark>
    <down_quark>%(DN_QUARK)s_MP</down_quark>
  </NamedObject>
</elem>

<elem>
<Name>MESON_CONTRACTIONS</Name>
<MesonParams>
<p2_max>0</p2_max>
<particle_list>
  <elem>piplus</elem>
</particle_list>
<h5_file_name>%(MRES_FILE)s</h5_file_name>
<obj_path>/pseudo_pseudo_UU</obj_path>
</MesonParams>
  <NamedObject>
    <up_quark>%(UP_QUARK)s</up_quark>
    <down_quark>%(UP_QUARK)s</down_quark>
  </NamedObject>
</elem>

<elem>
<Name>MESON_CONTRACTIONS</Name>
<MesonParams>
<p2_max>0</p2_max>
<particle_list>
  <elem>piplus</elem>
</particle_list>
<h5_file_name>%(MRES_FILE)s</h5_file_name>
<obj_path>/midpoint_pseudo_UU</obj_path>
</MesonParams>
  <NamedObject>
    <up_quark>%(UP_QUARK)s_MP</up_quark>
    <down_quark>%(UP_QUARK)s_MP</down_quark>
  </NamedObject>
</elem>

<elem>
<Name>MESON_CONTRACTIONS</Name>
<MesonParams>
<p2_max>0</p2_max>
<particle_list>
  <elem>piplus</elem>
</particle_list>
<h5_file_name>%(MRES_FILE)s</h5_file_name>
<obj_path>/pseudo_pseudo_DD</obj_path>
</MesonParams>
  <NamedObject>
    <up_quark>%(DN_QUARK)s</up_quark>
    <down_quark>%(DN_QUARK)s</down_quark>
  </NamedObject>
</elem>

<elem>
<Name>MESON_CONTRACTIONS</Name>
<MesonParams>
<p2_max>0</p2_max>
<particle_list>
  <elem>piplus</elem>
</particle_list>
<h5_file_name>%(MRES_FILE)s</h5_file_name>
<obj_path>/midpoint_pseudo_DD</obj_path>
</MesonParams>
  <NamedObject>
    <up_quark>%(DN_QUARK)s_MP</up_quark>
    <down_quark>%(DN_QUARK)s_MP</down_quark>
  </NamedObject>
</elem>

'''


meson_spec='''<elem>
<Name>MESON_CONTRACTIONS</Name>
<MesonParams>
<p2_max>2</p2_max>
<particle_list>
    <elem>octet_iso</elem>
</particle_list>
<h5_file_name>%(SPEC_FILE)s</h5_file_name>
<obj_path>/pt</obj_path>
</MesonParams>
  <NamedObject>
    <up_quark>%(UP_QUARK)s</up_quark>
    <down_quark>%(DN_QUARK)s</down_quark>
    <strange_quark>%(STRANGE_QUARK)s</strange_quark>
  </NamedObject>
</elem>

'''

baryon_spec = '''  <elem>
<Name>BARYON_CONTRACTIONS</Name>
<Frequency>1</Frequency>
<BaryonParams>
    <ng_parity>true</ng_parity>
    <h5_file_name>%(SPEC_FILE)s</h5_file_name>
    <path>/pt</path>
    <p2_max>2</p2_max>
    <particle_list>
        <elem>octet_iso</elem>
        <elem>decuplet_iso</elem>
    </particle_list>
</BaryonParams>
<NamedObject>
    <up_quark>%(UP_QUARK)s</up_quark>
    <down_quark>%(DN_QUARK)s</down_quark>
    <strange_quark>%(STRANGE_QUARK)s</strange_quark>
</NamedObject>
</elem>

'''

meson_meson = '''<elem>
  <Name>PIPI_SCATTERING</Name>
  <PipiParams>
    <p2_max>%(MM_REL_MOM)s</p2_max>
    <ptot2_max>%(MM_TOT_MOM)s</ptot2_max>
    <diagrams>0</diagrams>
    <h5_file_name>%(PIPI_SCAT_FILE)s</h5_file_name>
    <obj_path>/%(H5_PATH)s</obj_path>
  </PipiParams>
  <NamedObject>
    <up_quark>%(UP_QUARK)s</up_quark>
    <down_quark>%(DN_QUARK)s</down_quark>
    <strange_quark>%(STRANGE_QUARK)s</strange_quark>
  </NamedObject>
</elem>
'''

meson_meson_iso = '''<elem>
  <Name>PIPI_SCATTERING</Name>
  <PipiParams>
    <p2_max>%(MM_REL_MOM)s</p2_max>
    <ptot2_max>%(MM_TOT_MOM)s</ptot2_max>
    <diagrams>0</diagrams>
    <h5_file_name>%(PIPI_SCAT_FILE)s</h5_file_name>
    <obj_path>/%(H5_PATH)s</obj_path>
  </PipiParams>
  <NamedObject>
    <up_quark>%(UP_QUARK)s</up_quark>
    <strange_quark>%(STRANGE_QUARK)s</strange_quark>
  </NamedObject>
</elem>

'''


