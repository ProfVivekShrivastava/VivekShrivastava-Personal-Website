from bs4 import BeautifulSoup
import json

html = """
<table id="gsc_a_t">
    <thead>
        <tr id="gsc_a_tr0" aria-hidden="true">
            <th class="gsc_a_t"></th>
            <th class="gsc_a_c"></th>
            <th class="gsc_a_y"></th>
        </tr>
        <tr id="gsc_a_trh">
            <th class="gsc_a_t" scope="col">
                <span id="gsc_a_ta">Title</span>
                <div id="gsc_dd_sort-r" class="gs_md_r gs_md_rmb gs_md_rmbl">
                    <button
                        type="button"
                        id="gsc_dd_sort-b"
                        aria-controls="gsc_dd_sort-d"
                        aria-haspopup="true"
                        ontouchstart="gs_evt_dsp(event)"
                        class="gs_in_se gs_btn_mnu gs_btn_flat gs_btn_lrge gs_btn_half gs_btn_lsu gs_press gs_md_tb"
                    >
                        <span class="gs_wr"><span class="gs_lbl">Sort</span><span class="gs_icm"></span></span>
                    </button>
                    <div id="gsc_dd_sort-d" class="gs_md_d gs_md_ds gs_md_ulr" role="menu" tabindex="-1">
                        <div id="gsc_dd_sort-s" class="gs_oph gsc_dd_sec gsc_dd_sep">
                            <a
                                role="menuitem"
                                href="/citations?hl=en&amp;user=xR0COBoAAAAJ&amp;view_op=list_works"
                                tabindex="-1"
                                class="gs_md_li"
                                >Sort by citations</a
                            ><a
                                role="menuitem"
                                href="/citations?hl=en&amp;user=xR0COBoAAAAJ&amp;view_op=list_works&amp;sortby=pubdate"
                                tabindex="-1"
                                class="gs_md_li"
                                >Sort by year</a
                            ><a
                                role="menuitem"
                                href="/citations?hl=en&amp;user=xR0COBoAAAAJ&amp;view_op=list_works&amp;sortby=title"
                                tabindex="-1"
                                class="gs_md_li gsc_dd_sort-sel"
                                >Sort by title</a
                            >
                        </div>
                    </div>
                </div>
            </th>
            <th class="gsc_a_c" scope="col" dir="rtl">
                <span id="gsc_a_ca"
                    ><div class="gs_nph">
                        <a href="/citations?hl=en&amp;user=xR0COBoAAAAJ&amp;view_op=list_works" class="gsc_a_a"
                            >Cited by</a
                        >
                    </div>
                    <div class="gs_oph">Cited by</div></span
                >
            </th>
            <th class="gsc_a_y" scope="col">
                <span class="gsc_a_h" id="gsc_a_ha"
                    ><a
                        href="/citations?hl=en&amp;user=xR0COBoAAAAJ&amp;view_op=list_works&amp;sortby=pubdate"
                        class="gsc_a_a"
                        >Year</a
                    ></span
                >
            </th>
        </tr>
    </thead>
    <tbody id="gsc_a_b">
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:kw52XkFRtyQC"
                    class="gsc_a_at"
                    >A Decision-Making Framework for Electromagnetic Pulse Hardening Prioritisation of Critical
                    Facilities</a
                >
                <div class="gs_gray">VS Sumit Tomar, Manoj Kumawat</div>
                <div class="gs_gray">
                    Defence Science Journal, 76 (No. 2 (2026)), 284-291<span class="gs_oph">, 2026</span>
                </div>
            </td>
            <td class="gsc_a_c"><a href="" class="gsc_a_ac gs_ibl"></a></td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2026</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:1taIhTC69MYC"
                    class="gsc_a_at"
                    >A Decision-Making Framework for Electromagnetic Pulse Hardening Prioritisation of Critical
                    Facilities</a
                >
                <div class="gs_gray"></div>
                <div class="gs_gray"></div>
            </td>
            <td class="gsc_a_c"><a href="" class="gsc_a_ac gs_ibl"></a></td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl"></span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:MpfHP-DdYjUC"
                    class="gsc_a_at"
                    >A Case Study on Corrective Measures of Secondary Control Assisted Microgrids.</a
                >
                <div class="gs_gray">S Bhambri, V Shrivastava, M Kumawat</div>
                <div class="gs_gray">International Energy Journal 25, 153<span class="gs_oph">, 2025</span></div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=2865860719945147914"
                    class="gsc_a_ac gs_ibl"
                    >2</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2025</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:K3LRdlH-MEoC"
                    class="gsc_a_at"
                    >A comparative study of maximum power point tracking methods for a photovoltaic-based water pumping
                    system</a
                >
                <div class="gs_gray">B Kumar, YK Chauhan, V Shrivastava</div>
                <div class="gs_gray">
                    International Journal of Sustainable Energy 33 (4), 797-810<span class="gs_oph">, 2014</span>
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=5961056462901514886"
                    class="gsc_a_ac gs_ibl"
                    >42</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2014</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:j7_hQOaDUrUC"
                    class="gsc_a_at"
                    >A comparative study of maximum power point tracking methods for a photovoltaic-based water pumping
                    system.</a
                >
                <div class="gs_gray">BK Bhavnesh Kumar, YK Chauhan, VS Vivek Shrivastava</div>
                <div class="gs_gray"></div>
            </td>
            <td class="gsc_a_c"><a href="" class="gsc_a_ac gs_ibl"></a></td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2014</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:4vMrXwiscB8C"
                    class="gsc_a_at"
                    >A Comprehensive Study on Electricity Theft Detection Using Data Analysis</a
                >
                <div class="gs_gray">T Sharma, V Shrivastava, M Kumawat</div>
                <div class="gs_gray">
                    2022 IEEE 10th Power India International Conference (PIICON)<span class="gs_oph">, 2023</span>
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=11806656898880204650"
                    class="gsc_a_ac gs_ibl"
                    >1</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2023</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:u-coK7KVo8oC"
                    class="gsc_a_at"
                    >A computational examination of lead free Cs2PtI6 based perovskite solar cell with investigation of
                    several carrier transport materials</a
                >
                <div class="gs_gray">NK Singh, A Agarwal, V Shrivastava, LK Awasthi</div>
                <div class="gs_gray">
                    Solar Energy Materials and Solar Cells 282, 113430<span class="gs_oph">, 2025</span>
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=10036480664430450431"
                    class="gsc_a_ac gs_ibl"
                    >15</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2025</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:nrtMV_XWKgEC"
                    class="gsc_a_at"
                    >A fuzzy logic based sensorless induction motor drive supplied from a photovoltaic source</a
                >
                <div class="gs_gray">VS B Kumar, YK Chauhan</div>
                <div class="gs_gray">
                    2013 Annual International Conference on Emerging Research Areas and 2013&nbsp;…<span class="gs_oph"
                        >, 2013</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=462849219918591190"
                    class="gsc_a_ac gs_ibl"
                    >5</a
                ><span class="gsc_a_m"
                    ><a href="javascript:void(0)" class="gsc_a_am" data-eid="xR0COBoAAAAJ:nrtMV_XWKgEC">*</a></span
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2013</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:LPZeul_q3PIC"
                    class="gsc_a_at"
                    >A novel approach of input variable selection for ANN based load forecasting</a
                >
                <div class="gs_gray">V Shrivastava, RB Misra</div>
                <div class="gs_gray">
                    2008 Joint International Conference on Power System Technology and IEEE&nbsp;…<span class="gs_oph"
                        >, 2008</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=9818049720704232562"
                    class="gsc_a_ac gs_ibl"
                    >17</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2008</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:p__nRnzSRKYC"
                    class="gsc_a_at"
                    >A PSO based search for optimal tuning and fixing of UPFC to improve usefulness of distribution
                    system</a
                >
                <div class="gs_gray">SP Jaiswal, V Shrivastava</div>
                <div class="gs_gray">
                    Journal of Intelligent &amp; Fuzzy Systems 35 (5), 4987-4995<span class="gs_oph">, 2018</span>
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=133808637195819234"
                    class="gsc_a_ac gs_ibl"
                    >15</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2018</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:DJbcl8HfkQkC"
                    class="gsc_a_at"
                    >A Review of Li-Ion Battery's Thermal Runaway Mitigation Strategies with an Eye towards a Smarter
                    BTMS</a
                >
                <div class="gs_gray">B Kasniya, T Kanumuri, V Shrivastava, V Sharma</div>
                <div class="gs_gray">
                    2022 IEEE 10th Power India International Conference (PIICON)<span class="gs_oph">, 2023</span>
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=12985973042665949904"
                    class="gsc_a_ac gs_ibl"
                    >9</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2023</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:XiVPGOgt02cC"
                    class="gsc_a_at"
                    >A review on distributed generation definitions and DG impacts on distribution system</a
                >
                <div class="gs_gray">VS Bhadoria, NS Pal, V Shrivastava</div>
                <div class="gs_gray">
                    Proc. Int. Conf. Advanced Computing and Communication Technologies (ICACCT&nbsp;…<span
                        class="gs_oph"
                        >, 2013</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=12420251451432130913"
                    class="gsc_a_ac gs_ibl"
                    >56</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2013</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:umqufdRvDiIC"
                    class="gsc_a_at"
                    >A Review: Integration of Distributed Generation in Distribution System</a
                >
                <div class="gs_gray">A Chowdhury, SK Bihari, SP Jaiswal, V Shrivastava</div>
                <div class="gs_gray"></div>
            </td>
            <td class="gsc_a_c"><a href="" class="gsc_a_ac gs_ibl"></a></td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2017</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:foquWX3nUaYC"
                    class="gsc_a_at"
                    >A Wideband Star-Shaped Rectenna for RF Energy Harvesting in GSM Band</a
                >
                <div class="gs_gray">V Singh, VS Pandey, V Shrivastava</div>
                <div class="gs_gray">
                    Advances in Electromechanical Technologies: Select Proceedings of TEMT 2019&nbsp;…<span
                        class="gs_oph"
                        >, 2020</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=9788880728810060591"
                    class="gsc_a_ac gs_ibl"
                    >5</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2020</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:b1wdh0AR-JQC"
                    class="gsc_a_at"
                    >Accelerated life testing and performance evaluation of smart pressure transmitters for use in
                    nuclear power plants</a
                >
                <div class="gs_gray">Y Chauhan, NB Shrestha, TV Santhosh, V Shrivastava, PK Ramteke, ...</div>
                <div class="gs_gray">
                    2018 7th International Conference on Reliability, Infocom Technologies and&nbsp;…<span
                        class="gs_oph"
                        >, 2018</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=14363596423653588494"
                    class="gsc_a_ac gs_ibl"
                    >4</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2018</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:cWzG1nlazyYC"
                    class="gsc_a_at"
                    >Advance deep convolution neural network for multiple fault diagnosis of induction motor</a
                >
                <div class="gs_gray">R Jigyasu, V Shrivastava, S Singh</div>
                <div class="gs_gray">
                    2022 IEEE 10th Power India International Conference (PIICON)<span class="gs_oph">, 2023</span>
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=15082528325656572908"
                    class="gsc_a_ac gs_ibl"
                    >10</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2023</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:nRpfm8aw39MC"
                    class="gsc_a_at"
                    >Advancing Battery Safety: Machine Learning-Driven Thermal Management and Cloud-Based Analytics.</a
                >
                <div class="gs_gray">B Kasniya, T Kanumuri, V Shrivastava</div>
                <div class="gs_gray">International Energy Journal 25 (3), 389<span class="gs_oph">, 2025</span></div>
            </td>
            <td class="gsc_a_c"><a href="" class="gsc_a_ac gs_ibl"></a></td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2025</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:wbdj-CoPYUoC"
                    class="gsc_a_at"
                    >Allocation of UPFC in distribution system to minimize the losses</a
                >
                <div class="gs_gray">SP Jaiswal, V Shrivastava</div>
                <div class="gs_gray">
                    2014 Innovative Applications of Computational Intelligence on Power, Energy&nbsp;…<span
                        class="gs_oph"
                        >, 2014</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=14559952104585344529"
                    class="gsc_a_ac gs_ibl"
                    >15</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2014</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:BJbdYPG6LGMC"
                    class="gsc_a_at"
                    >An Approach to Optimize Query Using Rank Aware Scoring Function</a
                >
                <div class="gs_gray">V Shrivastava, B Patel</div>
                <div class="gs_gray">
                    2013 5th International Conference and Computational Intelligence and&nbsp;…<span class="gs_oph"
                        >, 2013</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=3462893296226815225"
                    class="gsc_a_ac gs_ibl"
                    >1</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2013</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:eJXPG6dFmWUC"
                    class="gsc_a_at"
                    >An assessment of electrical load forecasting using artificial neural network</a
                >
                <div class="gs_gray">V Shrivastava, RB Misra, RC Bansal</div>
                <div class="gs_gray">
                    International Journal of Computer Aided Engineering and Technology 4 (1), 80-89<span class="gs_oph"
                        >, 2012</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=6067146675944235134"
                    class="gsc_a_ac gs_ibl"
                    >4</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2012</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:0izLItjtcgwC"
                    class="gsc_a_at"
                    >An Assessment of Two-Dimensional Warranty Forecasting Model</a
                >
                <div class="gs_gray">ST Shrivastava Vivek</div>
                <div class="gs_gray">
                    International Conference on Reliability Safety &amp; Quality Engineering (ICRSQE&nbsp;…<span
                        class="gs_oph"
                        >, 2008</span
                    >
                </div>
            </td>
            <td class="gsc_a_c"><a href="" class="gsc_a_ac gs_ibl"></a></td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2008</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:W5xh706n7nkC"
                    class="gsc_a_at"
                    >An improve efficiency of li-ion batteries using optimization technique</a
                >
                <div class="gs_gray">N Swal, V Shrivastava</div>
                <div class="gs_gray">
                    2016 3rd International Conference on Computing for Sustainable Global&nbsp;…<span class="gs_oph"
                        >, 2016</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=6601041194122951399"
                    class="gsc_a_ac gs_ibl"
                    >2</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2016</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:uLbwQdceFCQC"
                    class="gsc_a_at"
                    >An improve efficiency of li-ion batteries with harmony search algorithm</a
                >
                <div class="gs_gray">N Swal, V Shrivastava</div>
                <div class="gs_gray">
                    2016 International Conference on Energy Efficient Technologies for&nbsp;…<span class="gs_oph"
                        >, 2016</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=6398511424896169559"
                    class="gsc_a_ac gs_ibl"
                    >1</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2016</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:tKAzc9rXhukC"
                    class="gsc_a_at"
                    >Analysis of boost converter with input source power conditioning</a
                >
                <div class="gs_gray">SK Sharma, DK Palwalia, V Shrivastava</div>
                <div class="gs_gray">
                    2016 IEEE 1st International Conference on Power Electronics, Intelligent&nbsp;…<span class="gs_oph"
                        >, 2016</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=2178580314412933550"
                    class="gsc_a_ac gs_ibl"
                    >6</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2016</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:7T2F9Uy0os0C"
                    class="gsc_a_at"
                    >Analysis of Energy Storage System for Wind Power Generation with application of Bidirectional
                    Converter</a
                >
                <div class="gs_gray">A Aroliya, S Gautam, A Kumar, V Shrivastava</div>
                <div class="gs_gray">
                    2016 Second International Conference on Computational Intelligence&nbsp;…<span class="gs_oph"
                        >, 2016</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=7018821519778472509"
                    class="gsc_a_ac gs_ibl"
                    >5</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2016</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:4fGpz3EwCPoC"
                    class="gsc_a_at"
                    >Analysis of Various Conditional Configuration of Load Bus using Method of Moment</a
                >
                <div class="gs_gray"></div>
                <div class="gs_gray">
                    Communications in dependability and quality management: an international&nbsp;…<span class="gs_oph"
                        >, 2008</span
                    >
                </div>
            </td>
            <td class="gsc_a_c"><a href="" class="gsc_a_ac gs_ibl"></a></td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2008</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:uJ-U7cs_P_0C"
                    class="gsc_a_at"
                    >Analytical behavior of brushless doubly fed electric variable transmission for wind power
                    generation</a
                >
                <div class="gs_gray">A Kumar, S Mishra, V Shrivastava, R Bansal</div>
                <div class="gs_gray">
                    International Transactions on Electrical Energy Systems 27 (12), e2453<span class="gs_oph"
                        >, 2017</span
                    >
                </div>
            </td>
            <td class="gsc_a_c"><a href="" class="gsc_a_ac gs_ibl"></a></td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2017</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:WC23djZS0W4C"
                    class="gsc_a_at"
                    >Analyzing Loss Mechanism of High Frequency Ferrite Core Transformer in Power Electronics Based
                    Converter</a
                >
                <div class="gs_gray">V Shrivastava, S Bhambri, M Kumawat</div>
                <div class="gs_gray">
                    Frontiers of Multidisciplinary Research 1 (3)<span class="gs_oph">, 2026</span>
                </div>
            </td>
            <td class="gsc_a_c"><a href="" class="gsc_a_ac gs_ibl"></a></td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2026</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:5qfkUJPXOUwC"
                    class="gsc_a_at"
                    >Application of modified clonal PSO in distributed generator placement for enhancement of efficiency
                    and voltage stability in distribution system</a
                >
                <div class="gs_gray">VS Bhadoria, SP Jaiswal, NS Pal, V Shrivastava</div>
                <div class="gs_gray">
                    Advances in Energy Technology: Select Proceedings of EMSME 2020, 703-718<span class="gs_oph"
                        >, 2021</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=244563380223377660"
                    class="gsc_a_ac gs_ibl"
                    >3</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2021</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:ruyezt5ZtCIC"
                    class="gsc_a_at"
                    >Applications of meta-heuristics in renewable energy systems</a
                >
                <div class="gs_gray">M Kumawat, N Gupta, N Jain, V Shrivastava, G Sharma</div>
                <div class="gs_gray">
                    Metaheuristic and Evolutionary Computation: Algorithms and Applications, 253-282<span class="gs_oph"
                        >, 2020</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=15593084195896198173"
                    class="gsc_a_ac gs_ibl"
                    >4</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2020</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:TIZ-Mc8IlK0C"
                    class="gsc_a_at"
                    >Artificial immune system based approach for size and location optimization of distributed
                    generation in distribution system</a
                >
                <div class="gs_gray">VS Bhadoria, NS Pal, V Shrivastava</div>
                <div class="gs_gray">
                    International Journal of System Assurance Engineering and Management 10 (3&nbsp;…<span
                        class="gs_oph"
                        >, 2019</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=9652157384776099667"
                    class="gsc_a_ac gs_ibl"
                    >35</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2019</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:IUKN3-7HHlwC"
                    class="gsc_a_at"
                    >Artificial Intelligence for Solar Photovoltaic Systems: Approaches, Methodologies, and
                    Technologies</a
                >
                <div class="gs_gray">B Kumar, B Pratap, V Shrivastava</div>
                <div class="gs_gray">CRC Press<span class="gs_oph">, 2022</span></div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=6872016417906195689"
                    class="gsc_a_ac gs_ibl"
                    >4</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2022</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:BrmTIyaxlBUC"
                    class="gsc_a_at"
                    >Assessment of a fuzzy logic based MRAS observer used in a photovoltaic array supplied AC drive</a
                >
                <div class="gs_gray">B Kumar, YK Chauhan, V Shrivastava</div>
                <div class="gs_gray">Frontiers in Energy 8 (1), 81-89<span class="gs_oph">, 2014</span></div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=12759438456759958068"
                    class="gsc_a_ac gs_ibl"
                    >16</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2014</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:PaBasH6fAo0C"
                    class="gsc_a_at"
                    >Augmented networks component importance measure under common cause failures</a
                >
                <div class="gs_gray">K Hazarika, VS Bhadoria, M Khemariya, V Shrivastava</div>
                <div class="gs_gray">
                    International Journal of System Assurance Engineering and Management 16 (12&nbsp;…<span
                        class="gs_oph"
                        >, 2025</span
                    >
                </div>
            </td>
            <td class="gsc_a_c"><a href="" class="gsc_a_ac gs_ibl"></a></td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2025</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:MhiOAD_qIWkC"
                    class="gsc_a_at"
                    >Baseline Modeling and Comparative Evaluation of Control Strategies for Utility-Tied and Islanded
                    Microgrid with Bidirectional Electric Vehicle Integration</a
                >
                <div class="gs_gray">P Bisht, V Shrivastava, R Kumar</div>
                <div class="gs_gray">
                    DMPedia Lecture Notes in Multidisciplinary Research, 628-643<span class="gs_oph">, 2026</span>
                </div>
            </td>
            <td class="gsc_a_c"><a href="" class="gsc_a_ac gs_ibl"></a></td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2026</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:4MWp96NkSFoC"
                    class="gsc_a_at"
                    >Battery energy storage technology integrated for power system reliability improvement</a
                >
                <div class="gs_gray">SR Ramavat, SP Jaiswal, N Goel, V Shrivastava</div>
                <div class="gs_gray">
                    Advances in Energy and Power Systems: Select Proceedings of ICAEDC 2017, 131-140<span class="gs_oph"
                        >, 2018</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=14941644839691350148"
                    class="gsc_a_ac gs_ibl"
                    >17</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2018</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:LI9QrySNdTsC"
                    class="gsc_a_at"
                    >Bayesian belief network as a tool for load forecasting</a
                >
                <div class="gs_gray">V Shrivastava</div>
                <div class="gs_gray"></div>
            </td>
            <td class="gsc_a_c"><a href="" class="gsc_a_ac gs_ibl"></a></td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2009</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:dBIO0h50nwkC"
                    class="gsc_a_at"
                    >Bidirectional Converter for V2G Application of Reactive Power Compensation</a
                >
                <div class="gs_gray">DSC Aditya, MT Student, V Shrivastava</div>
                <div class="gs_gray">
                    2022 IEEE 10th Power India International Conference (PIICON)<span class="gs_oph">, 2023</span>
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=14392569612881954192"
                    class="gsc_a_ac gs_ibl"
                    >5</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2023</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:2tRrZ1ZAMYUC"
                    class="gsc_a_at"
                    >Biological approaches to nanoparticles synthesis and their applications in the development of
                    herbal formulations</a
                >
                <div class="gs_gray">V Shrivastava, B Patel, AK Jain</div>
                <div class="gs_gray">
                    Nanoparticles and Nanocarriers Based Pharmaceutical Preparations, 436-454<span class="gs_oph"
                        >, 2022</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=5518961502485933355"
                    class="gsc_a_ac gs_ibl"
                    >3</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2022</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:9c2xU6iGI7YC"
                    class="gsc_a_at"
                    >Candidate project selection in cross project defect prediction using hybrid method</a
                >
                <div class="gs_gray">S Kanwar, LK Awasthi, V Shrivastava</div>
                <div class="gs_gray">
                    Expert Systems with Applications 218, 119625<span class="gs_oph">, 2023</span>
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=6297061713796041119"
                    class="gsc_a_ac gs_ibl"
                    >21</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2023</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:IRz6iEL74y4C"
                    class="gsc_a_at"
                    >Case Study on Modernization of a Micro-Grid and Its Performance Analysis Employing Solar PV
                    Units</a
                >
                <div class="gs_gray">SP Jaiswal, VS Bhadoria, R Singh, V Shrivastava, A Ambikapathy</div>
                <div class="gs_gray">Energy Harvesting, 81-104<span class="gs_oph">, 2022</span></div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=2474603085556682402"
                    class="gsc_a_ac gs_ibl"
                    >112</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2022</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:Ehil0879vHcC"
                    class="gsc_a_at"
                    >Communication and Intelligent Systems</a
                >
                <div class="gs_gray">H Sharma, V Shrivastava, KK Bharti, L Wang</div>
                <div class="gs_gray">Proceedings of ICCIS 1<span class="gs_oph">, 2022</span></div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=5779569753997113201"
                    class="gsc_a_ac gs_ibl"
                    >2</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2022</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:P7Ujq4OLJYoC"
                    class="gsc_a_at"
                    >Communication and Intelligent Systems</a
                >
                <div class="gs_gray">H Sharma, V Shrivastava, AK Tripathi, L Wang</div>
                <div class="gs_gray">Proceedings of ICCIS 1<span class="gs_oph">, 2024</span></div>
            </td>
            <td class="gsc_a_c"><a href="" class="gsc_a_ac gs_ibl"></a></td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2024</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:lvd772isFD0C"
                    class="gsc_a_at"
                    >Communication and Intelligent Systems: Proceedings of ICCIS 2022, Volume 2</a
                >
                <div class="gs_gray">KK Bharti, H Sharma, V Shrivastava, L Wang</div>
                <div class="gs_gray">Springer Verlag, Singapore<span class="gs_oph">, 2023</span></div>
            </td>
            <td class="gsc_a_c"><a href="" class="gsc_a_ac gs_ibl"></a></td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2023</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:UHK10RUVsp4C"
                    class="gsc_a_at"
                    >Comparison of analytical and heuristic techniques for multiobjective optimization in power
                    system</a
                >
                <div class="gs_gray">VS Bhadoria, NS Pal, V Shrivastava</div>
                <div class="gs_gray">
                    Problem Solving and Uncertainty Modeling through Optimization and Soft&nbsp;…<span class="gs_oph"
                        >, 2016</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=9275639552709046469"
                    class="gsc_a_ac gs_ibl"
                    >20</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2016</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:k8Z6L05lTy4C"
                    class="gsc_a_at"
                    >Comparison of Performance Analysis of Optimal Controllers for Frequency Regulation of Three-Area
                    Power System</a
                >
                <div class="gs_gray">S Vivek, VS Bhadoria, H Pulluri, Preeti</div>
                <div class="gs_gray">
                    Intelligent Computing Techniques for Smart Energy Systems, 735-743<span class="gs_oph">, 2020</span>
                </div>
            </td>
            <td class="gsc_a_c"><a href="" class="gsc_a_ac gs_ibl"></a></td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2020</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:86PQX7AUzd4C"
                    class="gsc_a_at"
                    >Compensation techniques to maintain the line parameters of traction power supply system using FACTS
                    device</a
                >
                <div class="gs_gray">C Vaishnav, L Singh, V Shrivastava</div>
                <div class="gs_gray">
                    2016 IEEE 7th Power India International Conference (PIICON), 1-5<span class="gs_oph">, 2016</span>
                </div>
            </td>
            <td class="gsc_a_c"><a href="" class="gsc_a_ac gs_ibl"></a></td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2016</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:2VqYfGB8ITEC"
                    class="gsc_a_at"
                    >Condition Monitoring of Power Electronic Devices-A Review</a
                >
                <div class="gs_gray">V Shrivastava</div>
                <div class="gs_gray">
                    2022 2nd International Conference on Advance Computing and Innovative&nbsp;…<span class="gs_oph"
                        >, 2022</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=10184305638819842314"
                    class="gsc_a_ac gs_ibl"
                    >10</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2022</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:mlAyqtXpCwEC"
                    class="gsc_a_at"
                    >Cross-Project Defect Prediction by Using Optimized Light Gradient Boosting Machine Algorithm</a
                >
                <div class="gs_gray">S Kanwar, LK Awasthi, V Shrivastava</div>
                <div class="gs_gray">
                    Communication and Intelligent Systems: Proceedings of ICCIS 2021, 933-946<span class="gs_oph"
                        >, 2022</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=3758636544364419705"
                    class="gsc_a_ac gs_ibl"
                    >2</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2022</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:OTTXONDVkokC"
                    class="gsc_a_at"
                    >Data Fusion-Based Smart Condition Monitoring of Critically Applied Rotating Machines</a
                >
                <div class="gs_gray">R Jigyasu, V Shrivastava, S Singh</div>
                <div class="gs_gray">
                    Proceedings of Third Doctoral Symposium on Computational Intelligence: DoSCI&nbsp;…<span
                        class="gs_oph"
                        >, 2022</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=15082752237863757739"
                    class="gsc_a_ac gs_ibl"
                    >4</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2022</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:OP4eGU-M3BUC"
                    class="gsc_a_at"
                    >Deep optimal feature extraction and selection-based motor fault diagnosis using vibration</a
                >
                <div class="gs_gray">R Jigyasu, V Shrivastava, S Singh</div>
                <div class="gs_gray">Electrical Engineering 106 (5), 6339-6358<span class="gs_oph">, 2024</span></div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=17208363699681273034"
                    class="gsc_a_ac gs_ibl"
                    >9</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2024</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:iH-uZ7U-co4C"
                    class="gsc_a_at"
                    >Delay testable enhanced scan flip-flop: Dft for high fault coverage</a
                >
                <div class="gs_gray">AK Suhag, V Shrivastava</div>
                <div class="gs_gray">
                    2011 International Symposium on Electronic System Design, 129-133<span class="gs_oph">, 2011</span>
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=7639051171721765484"
                    class="gsc_a_ac gs_ibl"
                    >14</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2011</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:XD-gHx7UXLsC"
                    class="gsc_a_at"
                    >Design and assessment of solar photovoltaic system for a village of Rajasthan</a
                >
                <div class="gs_gray">A Khandelwal, V Shrivastava</div>
                <div class="gs_gray">
                    2017 International Conference on Circuit, Power and Computing Technologies&nbsp;…<span
                        class="gs_oph"
                        >, 2017</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=5090215754731026465"
                    class="gsc_a_ac gs_ibl"
                    >3</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2017</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:QYdC8u9Cj1oC"
                    class="gsc_a_at"
                    >Design Methodology of Single and Multi-Winding Coupled Inductor in Switching Converters</a
                >
                <div class="gs_gray">S Bhambri, V Shrivastava, M Kumawat</div>
                <div class="gs_gray">
                    2022 IEEE 10th Power India International Conference (PIICON)<span class="gs_oph">, 2023</span>
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=10350505579654389409"
                    class="gsc_a_ac gs_ibl"
                    >5</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2023</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:yFnVuubrUp4C"
                    class="gsc_a_at"
                    >Design of Controller for Brushless DC Motor Using a Hybrid Optimization Technique</a
                >
                <div class="gs_gray">P Saini, P Thakur, RC Bansal, A Dixit, V Shrivastava, J Kumar</div>
                <div class="gs_gray">
                    2022 IEEE 10th Power India International Conference (PIICON)<span class="gs_oph">, 2023</span>
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=17224469380362015880"
                    class="gsc_a_ac gs_ibl"
                    >5</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2023</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:4fKUyHm3Qg0C"
                    class="gsc_a_at"
                    >Development of Bayesian belief network model for electrical load demand</a
                >
                <div class="gs_gray">V Shrivastava, RB Misra</div>
                <div class="gs_gray">
                    International Journal of Systems Assurance Engineering and Management 1 (2&nbsp;…<span
                        class="gs_oph"
                        >, 2010</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=3465395743385288599"
                    class="gsc_a_ac gs_ibl"
                    >10</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2010</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:_OXeSy2IsFwC"
                    class="gsc_a_at"
                    >DGA Based Transformer Fault Analysis Using Machine Learning</a
                >
                <div class="gs_gray">A Kumar, AR Saxena, V Shrivastava</div>
                <div class="gs_gray">
                    2024 International Conference on Electrical Electronics and Computing&nbsp;…<span class="gs_oph"
                        >, 2024</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=6775191886478486045"
                    class="gsc_a_ac gs_ibl"
                    >2</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2024</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:kuK5TVdYjLIC"
                    class="gsc_a_at"
                    >Distributed generation integration optimization using fuzzy logic controller.</a
                >
                <div class="gs_gray">SK Sharma, DK Palwalia, V Shrivastava</div>
                <div class="gs_gray">AIMS Energy 7 (3), 337<span class="gs_oph">, 2019</span></div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=6464899335445849877"
                    class="gsc_a_ac gs_ibl"
                    >19</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2019</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:fQNAKQ3IYiAC"
                    class="gsc_a_at"
                    >Early fault detection model using integrated and cost-effective test case prioritization</a
                >
                <div class="gs_gray">AK Pandey, V Shrivastava</div>
                <div class="gs_gray">
                    International Journal of System Assurance Engineering and Management 2 (1&nbsp;…<span class="gs_oph"
                        >, 2011</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=3605533258921845204"
                    class="gsc_a_ac gs_ibl"
                    >14</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2011</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:uWiczbcajpAC"
                    class="gsc_a_at"
                    >Economic comparison of solar PV and diesel water pumping system</a
                >
                <div class="gs_gray">G Dadhich, V Shrivastava</div>
                <div class="gs_gray">
                    2017 International Conference on Information, Communication, Instrumentation&nbsp;…<span
                        class="gs_oph"
                        >, 2017</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=2742798980111925981"
                    class="gsc_a_ac gs_ibl"
                    >18</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2017</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:MLfJN-KU85MC"
                    class="gsc_a_at"
                    >Economic viability solar PV power plant in distribution system</a
                >
                <div class="gs_gray">S Pujan Jaiswal, V Shrivastava, S Singh</div>
                <div class="gs_gray">
                    IOP Conference Series: Materials Science and Engineering 594 (1), 012010<span class="gs_oph"
                        >, 2019</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=14345786509803156391"
                    class="gsc_a_ac gs_ibl"
                    >11</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2019</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:TFP_iSt0sucC"
                    class="gsc_a_at"
                    >Efficacy of different rule based fuzzy logic controllers for induction motor drive</a
                >
                <div class="gs_gray">B Kumar, YK Chauhan, V Shrivastava</div>
                <div class="gs_gray">
                    International Journal of Machine Learning and Computing 2 (2), 131-137<span class="gs_oph"
                        >, 2012</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=14111279848554532451"
                    class="gsc_a_ac gs_ibl"
                    >25</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2012</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:LhH-TYMQEocC"
                    class="gsc_a_at"
                    >Efficient condition monitoring of off shore wind turbines using deep networks</a
                >
                <div class="gs_gray">R Jigyasu, V Shrivastava, S Singh</div>
                <div class="gs_gray">
                    2023 International Conference on Computer, Electronics &amp; Electrical&nbsp;…<span class="gs_oph"
                        >, 2023</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=14347802695286462059"
                    class="gsc_a_ac gs_ibl"
                    >1</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2023</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:ODE9OILHJdcC"
                    class="gsc_a_at"
                    >Efficient random forest algorithm for multi-objective optimization in software defect prediction</a
                >
                <div class="gs_gray">S Kanwar, LK Awasthi, V Shrivastava</div>
                <div class="gs_gray">IETE Journal of Research 70 (4), 3690-3702<span class="gs_oph">, 2024</span></div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=14637667883778090046"
                    class="gsc_a_ac gs_ibl"
                    >12</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2024</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:eflP2zaiRacC"
                    class="gsc_a_at"
                    >Elimination of output gating performance overhead for critical paths in scan test</a
                >
                <div class="gs_gray">AK Suhag, S Ahlawat, V Shrivastava, N Singh</div>
                <div class="gs_gray">
                    International Journal of Circuits and Architecture Design 1 (1), 62-73<span class="gs_oph"
                        >, 2013</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=7581931763498759373"
                    class="gsc_a_ac gs_ibl"
                    >10</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2013</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:7BrZ7Jt4UNcC"
                    class="gsc_a_at"
                    >Empowering the future: a comprehensive review of cutting‐edge battery technologies</a
                >
                <div class="gs_gray">B Kasniya, T Kanumuri, V Shriwastava, S Karan</div>
                <div class="gs_gray">
                    Materialwissenschaft und Werkstofftechnik 56 (6), 790-818<span class="gs_oph">, 2025</span>
                </div>
            </td>
            <td class="gsc_a_c"><a href="" class="gsc_a_ac gs_ibl"></a></td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2025</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:WHdLCjDvYFkC"
                    class="gsc_a_at"
                    >Enselect: a Robust Ensemble Feature Selection Method for Cross Project Defect Prediction</a
                >
                <div class="gs_gray">S Kanwar, LK Awasthi, V Shrivastava</div>
                <div class="gs_gray">
                    2026 International Conference on Computing, Sciences and Communications&nbsp;…<span class="gs_oph"
                        >, 2026</span
                    >
                </div>
            </td>
            <td class="gsc_a_c"><a href="" class="gsc_a_ac gs_ibl"></a></td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2026</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:_5tno0g5mFcC"
                    class="gsc_a_at"
                    >Feature Selection with Stochastic Hill-Climbing Algorithm in Cross Project Defect Prediction</a
                >
                <div class="gs_gray">S Kanwar, LK Awasthi, V Shrivastava</div>
                <div class="gs_gray">
                    2022 2nd International Conference on Advance Computing and Innovative&nbsp;…<span class="gs_oph"
                        >, 2022</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=1102436794465599284"
                    class="gsc_a_ac gs_ibl"
                    >3</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2022</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:bEWYMUwI8FkC"
                    class="gsc_a_at"
                    >Flip–flop selection for partial enhance scan chain using DTESFF for high transition delay fault
                    coverage</a
                >
                <div class="gs_gray">AK Suhag, V Shrivastava, N Singh</div>
                <div class="gs_gray">
                    International Journal of System Assurance Engineering and Management 4 (3&nbsp;…<span class="gs_oph"
                        >, 2013</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=6121831548668590362"
                    class="gsc_a_ac gs_ibl"
                    >4</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2013</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:VaXvl8Fpj5cC"
                    class="gsc_a_at"
                    >Fuzzy Logic Based Analysis of Dissolved Decay Contents in Transformer Oil</a
                >
                <div class="gs_gray">N Ghosh, VS Bhadoria, RN Sharma, V Shrivastava</div>
                <div class="gs_gray">
                    Advances in RAMS Engineering: In Honor of Professor Ajit Kumar Verma on His&nbsp;…<span
                        class="gs_oph"
                        >, 2019</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=12296328870872905216"
                    class="gsc_a_ac gs_ibl"
                    >2</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2019</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:HIFyuExEbWQC"
                    class="gsc_a_at"
                    >Grid Integrated 10kW Solar Photovoltaic System Using Conventional Controlling Techniques</a
                >
                <div class="gs_gray">DS Govind, A Agarwal, V Shrivastava</div>
                <div class="gs_gray">
                    2022 IEEE 10th Power India International Conference (PIICON)<span class="gs_oph">, 2023</span>
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=9178381274660711314"
                    class="gsc_a_ac gs_ibl"
                    >7</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2023</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:FiytvqdAVhgC"
                    class="gsc_a_at"
                    >GRU-Powered Cloud Framework for Advanced Analytics of lithium iron phosphate Cell</a
                >
                <div class="gs_gray">B Kasniya, T Kanumuri, V Shrivastava</div>
                <div class="gs_gray">
                    2025 IEEE 5th International Conference on Sustainable Energy and Future&nbsp;…<span class="gs_oph"
                        >, 2025</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=13519683651587393269"
                    class="gsc_a_ac gs_ibl"
                    >1</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2025</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:1lhNe0rCu4AC"
                    class="gsc_a_at"
                    >Guardians of Energy: A Machine Learning Approach to Enhance Battery Safety</a
                >
                <div class="gs_gray">T Kanumuri, V Shrivastava</div>
                <div class="gs_gray"></div>
            </td>
            <td class="gsc_a_c"><a href="" class="gsc_a_ac gs_ibl"></a></td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl"></span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:OcBU2YAGkTUC"
                    class="gsc_a_at"
                    >Hybrid multi-model feature fusion-based vibration monitoring for rotating machine fault
                    diagnosis</a
                >
                <div class="gs_gray">R Jigyasu, V Shrivastava, S Singh</div>
                <div class="gs_gray">
                    Journal of Vibration Engineering &amp; Technologies 12 (3), 2791-2810<span class="gs_oph"
                        >, 2024</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=2535817002527773424"
                    class="gsc_a_ac gs_ibl"
                    >13</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2024</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:GFxP56DSvIMC"
                    class="gsc_a_at"
                    >Illuminating Urban Landscapes using IoT Based Approach for Smart Street Lighting</a
                >
                <div class="gs_gray">S Gupta, S Mehta, V Shrivastava, AK Singh</div>
                <div class="gs_gray">
                    2024 3rd International Conference on Artificial Intelligence For Internet of&nbsp;…<span
                        class="gs_oph"
                        >, 2024</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=15952112820711971979"
                    class="gsc_a_ac gs_ibl"
                    >1</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2024</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:gsN89kCJA0AC"
                    class="gsc_a_at"
                    >Impact of semiconductor devices on voltage stability of distribution system</a
                >
                <div class="gs_gray">SP Jaiswal, V Shrivastava, DK Palwalia</div>
                <div class="gs_gray">Materials Today: Proceedings 12, 581-589<span class="gs_oph">, 2019</span></div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=2701132999233748279"
                    class="gsc_a_ac gs_ibl"
                    >16</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2019</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:_Ybze24A_UAC"
                    class="gsc_a_at"
                    >Improvement in efficiency of PV module using soft computing based MPPT</a
                >
                <div class="gs_gray">D Modani, V Shrivastava</div>
                <div class="gs_gray">
                    2016 3rd International Conference on Computing for Sustainable Global&nbsp;…<span class="gs_oph"
                        >, 2016</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=9602276135833705856"
                    class="gsc_a_ac gs_ibl"
                    >3</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2016</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:IaI1MmNe2tcC"
                    class="gsc_a_at"
                    >Improvement in power sharing performance in an AC microgrid through PI controller approach under
                    different load condition</a
                >
                <div class="gs_gray">S Bhambri, V Shrivastava, M Kumawat</div>
                <div class="gs_gray">
                    2025 IEEE 5th International Conference on Sustainable Energy and Future&nbsp;…<span class="gs_oph"
                        >, 2025</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=16358352776137794709"
                    class="gsc_a_ac gs_ibl"
                    >2</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2025</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:bnK-pcrLprsC"
                    class="gsc_a_at"
                    >Installation of DG for optimal demand compensation</a
                >
                <div class="gs_gray">VS Bhadoria, NS Pal, V Shrivastava</div>
                <div class="gs_gray">
                    2014 International Conference on Issues and Challenges in Intelligent&nbsp;…<span class="gs_oph"
                        >, 2014</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=9487721697562370155"
                    class="gsc_a_ac gs_ibl"
                    >14</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2014</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:OR75R8vi5nAC"
                    class="gsc_a_at"
                    >Installation of DG for Optimal Demand Compensation</a
                >
                <div class="gs_gray">V Shrivastava, VS Bhadoria, NS Pal</div>
                <div class="gs_gray"></div>
            </td>
            <td class="gsc_a_c"><a href="" class="gsc_a_ac gs_ibl"></a></td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl"></span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:mNrWkgRL2YcC"
                    class="gsc_a_at"
                    >Intelligent multiple fault diagnosis for predictive maintenance of induction motor</a
                >
                <div class="gs_gray">R Jigyasu, V Shrivastava, S Singh</div>
                <div class="gs_gray">
                    2022 IEEE 10th Power India International Conference (PIICON)<span class="gs_oph">, 2023</span>
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=16400021124076843243"
                    class="gsc_a_ac gs_ibl"
                    >3</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2023</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:kRWSkSYxWN8C"
                    class="gsc_a_at"
                    >Investigations on energy efficient sensorless induction motor drive</a
                >
                <div class="gs_gray">B Kumar, YK Chauhan, V Shrivastava</div>
                <div class="gs_gray">
                    International Conference on Computing, Communication &amp; Automation, 974-978<span class="gs_oph"
                        >, 2015</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=15611382529626312188"
                    class="gsc_a_ac gs_ibl"
                    >3</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2015</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:rmuvC79q63oC"
                    class="gsc_a_at"
                    >Leveraging controllability measures for high transition delay test coverage in DTESFF based partial
                    enhanced scan design</a
                >
                <div class="gs_gray">V Shrivastava, AK Suhag</div>
                <div class="gs_gray">
                    International Journal of System Assurance Engineering and Management 11 (3&nbsp;…<span
                        class="gs_oph"
                        >, 2020</span
                    >
                </div>
            </td>
            <td class="gsc_a_c"><a href="" class="gsc_a_ac gs_ibl"></a></td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2020</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:yqoGN6RLRZoC"
                    class="gsc_a_at"
                    >Lithium-Ion Battery’s SOH Estimation Using Machine Learning with Multi-Channel Charging Profiles</a
                >
                <div class="gs_gray">B Kasniya, T Kanumuri, V Shrivastava, Y Kuwal</div>
                <div class="gs_gray">
                    2023 International Conference on Computer, Electronics &amp; Electrical&nbsp;…<span class="gs_oph"
                        >, 2023</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=4804999584694891935"
                    class="gsc_a_ac gs_ibl"
                    >3</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2023</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:_FM0Bhl9EiAC"
                    class="gsc_a_at"
                    >Load Flow Analysis using Method of Moments</a
                >
                <div class="gs_gray">MRB Shrivastava Vivek</div>
                <div class="gs_gray">
                    Mathematical Modelling, Optimization and Their Applications (OPTIMA’07)<span class="gs_oph"
                        >, 2007</span
                    >
                </div>
            </td>
            <td class="gsc_a_c"><a href="" class="gsc_a_ac gs_ibl"></a></td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2007</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:7wO8s98CvbsC"
                    class="gsc_a_at"
                    >Modeling and Analysis of Restoration Control in Parallel Microsource Inverters: A Case Study</a
                >
                <div class="gs_gray">S Bhambri, V Shrivastava, M Kumawat</div>
                <div class="gs_gray">
                    Yanbu Journal of Engineering and Science 23 (1), 154-178<span class="gs_oph">, 2026</span>
                </div>
            </td>
            <td class="gsc_a_c"><a href="" class="gsc_a_ac gs_ibl"></a></td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2026</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:Aul-kAQHnToC"
                    class="gsc_a_at"
                    >Modelling and Control of Microgrids in an Offgrid Operating Scenario: A Case Study</a
                >
                <div class="gs_gray">S Bhambri, V Shrivastava, M Kumawat, S Agrawal</div>
                <div class="gs_gray">
                    2024 IEEE Region 10 Symposium (TENSYMP), 1-6<span class="gs_oph">, 2024</span>
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=17959250577156525233"
                    class="gsc_a_ac gs_ibl"
                    >4</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2024</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:0KyAp5RtaNEC"
                    class="gsc_a_at"
                    >Modelling of speed controller for industrial applications: a two mass drive system</a
                >
                <div class="gs_gray">S Choudhary, SK Sharma, V Shrivastava</div>
                <div class="gs_gray">
                    2016 IEEE 7th Power India International Conference (PIICON), 1-5<span class="gs_oph">, 2016</span>
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=4854995691814585398"
                    class="gsc_a_ac gs_ibl"
                    >6</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2016</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:8xutWZnSdmoC"
                    class="gsc_a_at"
                    >Non Invasive Fault Detection of Offshore Wind Turbines Using Deep Network-Based Thermogram
                    Features</a
                >
                <div class="gs_gray">R Jigyasu, V Shrivastava, S Singh</div>
                <div class="gs_gray">
                    Arabian Journal for Science and Engineering 49 (12), 16771-16794<span class="gs_oph">, 2024</span>
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=4111521659396764485"
                    class="gsc_a_ac gs_ibl"
                    >5</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2024</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:oNZyr7d5Mn4C"
                    class="gsc_a_at"
                    >Opportunities and challenges of PV technology in power system</a
                >
                <div class="gs_gray">SP Jaiswal, V Shrivastava, DK Palwalia</div>
                <div class="gs_gray">Materials Today: Proceedings 34, 593-597<span class="gs_oph">, 2021</span></div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=9361244582037703654"
                    class="gsc_a_ac gs_ibl"
                    >33</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2021</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:a3BOlSfXSfwC"
                    class="gsc_a_at"
                    >Optimal location and sizing of DG in distribution system and its cost-benefit analysis</a
                >
                <div class="gs_gray">SR Ramavt, N Goel, SP Jaiswal, V Shrivastava</div>
                <div class="gs_gray">
                    Advances in Intelligent Systems and Computing, Springer DOI 10, 978-981<span class="gs_oph"
                        >, 2019</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=11623795431556539687"
                    class="gsc_a_ac gs_ibl"
                    >6</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2019</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:L7CI7m0gUJcC"
                    class="gsc_a_at"
                    >Optimal location and sizing of DG in distribution system and its cost–benefit analysis</a
                >
                <div class="gs_gray">SR Ramavat, SP Jaiswal, N Goel, V Shrivastava</div>
                <div class="gs_gray">
                    Applications of Artificial Intelligence Techniques in Engineering: SIGMA&nbsp;…<span class="gs_oph"
                        >, 2018</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=14644553287119292001"
                    class="gsc_a_ac gs_ibl"
                    >18</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2018</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:YohjEiUPhakC"
                    class="gsc_a_at"
                    >Optimal Placement of DG for Reliability Improvement in Distribution System</a
                >
                <div class="gs_gray">A Singh, NS Pal, VS Bhadoria, V Shrivastava, AK Sihag</div>
                <div class="gs_gray">Dr. VK Gorana, Dr. Shiv Lal, 274<span class="gs_oph">, 2015</span></div>
            </td>
            <td class="gsc_a_c"><a href="" class="gsc_a_ac gs_ibl"></a></td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2015</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:ML0RJ9NH7IQC"
                    class="gsc_a_at"
                    >Optimal sitting and sizing of capacitor using iterative search method for enhancement of
                    reliability of distribution system</a
                >
                <div class="gs_gray">VS Bhadoria, NS Pal, V Shrivastava, SP Jaiswal</div>
                <div class="gs_gray">
                    Advances in Energy and Power Systems: Select Proceedings of ICAEDC 2017, 123-129<span class="gs_oph"
                        >, 2018</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=8562456924642398795"
                    class="gsc_a_ac gs_ibl"
                    >16</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2018</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:B3FOqHPlNUQC"
                    class="gsc_a_at"
                    >Output gating performance overhead elimination for scan test</a
                >
                <div class="gs_gray">AK Suhag, S Ahlawat, V Shrivastava, RR Choudhary</div>
                <div class="gs_gray">
                    International Journal of Electronics 102 (7), 1244-1252<span class="gs_oph">, 2015</span>
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=13485896371572520255"
                    class="gsc_a_ac gs_ibl"
                    >5</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2015</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:EkHepimYqZsC"
                    class="gsc_a_at"
                    >Particle swarm optimization of BLDC motor with fuzzy logic controller for speed improvement</a
                >
                <div class="gs_gray">S Agrawal, V Shrivastava</div>
                <div class="gs_gray">
                    2017 8th International Conference on Computing, Communication and Networking&nbsp;…<span
                        class="gs_oph"
                        >, 2017</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=11500045503547936563"
                    class="gsc_a_ac gs_ibl"
                    >15</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2017</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:08ZZubdj9fEC"
                    class="gsc_a_at"
                    >Performance analysis of a water pumping system supplied by a photovoltaic generator with different
                    maximum power point tracking techniques</a
                >
                <div class="gs_gray">B Kumar, YK Chauhan, V Shrivastava</div>
                <div class="gs_gray">
                    Songklanakarin J. Sci. Technol 36 (1), 107-113<span class="gs_oph">, 2014</span>
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=2742705212405177259"
                    class="gsc_a_ac gs_ibl"
                    >12</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2014</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:sNmaIFBj_lkC"
                    class="gsc_a_at"
                    >Performance analysis of electric vehicle motor controller with different controllers</a
                >
                <div class="gs_gray">S Agrawal, V Shrivastava</div>
                <div class="gs_gray">
                    Irisworld Proceedings of International Conference on Optical &amp; Wireless&nbsp;…<span
                        class="gs_oph"
                        >, 2017</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=6459606191658946956"
                    class="gsc_a_ac gs_ibl"
                    >2</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2017</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:XvxMoLDsR5gC"
                    class="gsc_a_at"
                    >Performance analysis of electric vehicle motor controller with different controllers</a
                >
                <div class="gs_gray"></div>
                <div class="gs_gray"></div>
            </td>
            <td class="gsc_a_c"><a href="" class="gsc_a_ac gs_ibl"></a></td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl"></span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=20&amp;pagesize=80&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:HbR8gkJAVGIC"
                    class="gsc_a_at"
                    >Performance analysis of fuzzy based sensorless induction motor drive with photovoltaic source</a
                >
                <div class="gs_gray">K Bhavnesh, CK Yogesh, V Shrivastava</div>
                <div class="gs_gray">
                    IEEE International Conference on Fuzzy Systems (FUZZ-IEEE), 1-6<span class="gs_oph">, 2013</span>
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=17433549435129742509"
                    class="gsc_a_ac gs_ibl"
                    >3</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2013</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=100&amp;pagesize=100&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:WZBGuue-350C"
                    class="gsc_a_at"
                    >Performance analysis of grid-connected 10.6 kW (commercial) solar PV power generation system</a
                >
                <div class="gs_gray">SK Sharma, DK Palwalia, V Shrivastava</div>
                <div class="gs_gray">Applied Solar Energy 55 (5), 269-281<span class="gs_oph">, 2019</span></div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=11747281219131192798"
                    class="gsc_a_ac gs_ibl"
                    >27</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2019</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=100&amp;pagesize=100&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:_axFR9aDTf0C"
                    class="gsc_a_at"
                    >Performance analysis of hybrid network of Indian traction power system using renewable energy
                    sources</a
                >
                <div class="gs_gray">L Singh, C Vaishnav, V Shrivastava</div>
                <div class="gs_gray">
                    2016 International Conference on Micro-Electronics and Telecommunication&nbsp;…<span class="gs_oph"
                        >, 2016</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=8389370957405270437"
                    class="gsc_a_ac gs_ibl"
                    >18</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2016</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=100&amp;pagesize=100&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:l7t_Zn2s7bgC"
                    class="gsc_a_at"
                    >Performance analysis of induction motor drive with optimal rotor flux for energy efficient
                    operation</a
                >
                <div class="gs_gray">B Kumar, YK Chauhan, V Shrivastava</div>
                <div class="gs_gray">
                    2014 IEEE International Conference on Advanced Communications, Control and&nbsp;…<span
                        class="gs_oph"
                        >, 2014</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=5264051763384205034"
                    class="gsc_a_ac gs_ibl"
                    >8</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2014</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=100&amp;pagesize=100&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:a9-T7VOCCH8C"
                    class="gsc_a_at"
                    >Performance and reliability investigation of practical microgrid with photovoltaic units</a
                >
                <div class="gs_gray">BUD Abdullah, SP Jaiswal, S Lata, S Dulal, V Shrivastava</div>
                <div class="gs_gray">
                    Artificial Intelligence for Solar Photovoltaic Systems: Approaches&nbsp;…<span class="gs_oph"
                        >, 2022</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=7507636730015175205"
                    class="gsc_a_ac gs_ibl"
                    >1</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2022</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=100&amp;pagesize=100&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:r0BpntZqJG4C"
                    class="gsc_a_at"
                    >Performance evaluation of delay testable enhanced scan flip-flop</a
                >
                <div class="gs_gray">AK Suhag, V Shrivastava</div>
                <div class="gs_gray">
                    International Journal of System Assurance Engineering and Management 3 (3&nbsp;…<span class="gs_oph"
                        >, 2012</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=13550073109983764668"
                    class="gsc_a_ac gs_ibl"
                    >5</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2012</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=100&amp;pagesize=100&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:sSrBHYA8nusC"
                    class="gsc_a_at"
                    >Performance Evaluation of Reduced Rule Base Fuzzy Logic Controller for Indirect Vector Controlled
                    Induction Motor Drive</a
                >
                <div class="gs_gray">B Kumar, YK Chauhan, V Shrivastava</div>
                <div class="gs_gray">
                    Proc. 4th International Conference on Computer Simulation and Modeling, 81-86<span class="gs_oph"
                        >, 2012</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=8509985829219470451"
                    class="gsc_a_ac gs_ibl"
                    >7</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2012</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=100&amp;pagesize=100&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:HtEfBTGE9r8C"
                    class="gsc_a_at"
                    >Performance Evaluation&nbsp;Of Reduced Rule Based Fuzzy Logic Controller For Vector Control
                    Induction Motor Drive</a
                >
                <div class="gs_gray">VS Bhavnesh Kumar, Yogesh Kumar Chauhan</div>
                <div class="gs_gray">
                    International Conference on “Computer Modeling and Simulation (ICCMS 2012) 4<span class="gs_oph"
                        >, 2012</span
                    >
                </div>
            </td>
            <td class="gsc_a_c"><a href="" class="gsc_a_ac gs_ibl"></a></td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2012</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=100&amp;pagesize=100&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:ZzlSgRqYykMC"
                    class="gsc_a_at"
                    >Performance Improvement in Droop Controlled Islanded Microgrids via Selective Harmonic Control</a
                >
                <div class="gs_gray">S Bhambri, V Shrivastava, M Kumawat</div>
                <div class="gs_gray">
                    2024 IEEE Third International Conference on Power Electronics, Intelligent&nbsp;…<span
                        class="gs_oph"
                        >, 2024</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=17970281349114322209"
                    class="gsc_a_ac gs_ibl"
                    >3</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2024</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=100&amp;pagesize=100&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:i2xiXl-TujoC"
                    class="gsc_a_at"
                    >Performance of smart pressure transmitters under radiation ageing environment in NPPs</a
                >
                <div class="gs_gray">Y Chauhan, NB Shrestha, TV Santhosh, V Shrivastava, PK Ramteke, ...</div>
                <div class="gs_gray">
                    International Journal of System Assurance Engineering and Management 11&nbsp;…<span class="gs_oph"
                        >, 2020</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=5843121024646735670"
                    class="gsc_a_ac gs_ibl"
                    >1</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2020</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=100&amp;pagesize=100&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:fbc8zXXH2BUC"
                    class="gsc_a_at"
                    >Power Engineering and Intelligent Systems</a
                >
                <div class="gs_gray">V Shrivastava, JC Bansal, BK Panigrahi</div>
                <div class="gs_gray">Proceedings of PEIS 1<span class="gs_oph">, 2023</span></div>
            </td>
            <td class="gsc_a_c"><a href="" class="gsc_a_ac gs_ibl"></a></td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2023</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=100&amp;pagesize=100&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:5MTHONV0fEkC"
                    class="gsc_a_at"
                    >Power Engineering and Intelligent Systems: Proceedings of PEIS 2025, Volume 1</a
                >
                <div class="gs_gray">JC Bansal, BK Panigrahi, V Shrivastava</div>
                <div class="gs_gray">Springer Nature Switzerland AG<span class="gs_oph">, 2026</span></div>
            </td>
            <td class="gsc_a_c"><a href="" class="gsc_a_ac gs_ibl"></a></td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2026</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=100&amp;pagesize=100&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:7H_MAutzIkAC"
                    class="gsc_a_at"
                    >Power Engineering and Intelligent Systems: Proceedings of PEIS 2025, Volume 3</a
                >
                <div class="gs_gray">V Shrivastava, Shrivastava</div>
                <div class="gs_gray">Springer<span class="gs_oph">, 2025</span></div>
            </td>
            <td class="gsc_a_c"><a href="" class="gsc_a_ac gs_ibl"></a></td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2025</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=100&amp;pagesize=100&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:bKqednn6t2AC"
                    class="gsc_a_at"
                    >Power Management &amp; Quality Analysis of Battery Storage Based Renewable Energy Generation System
                    for Utility Bus</a
                >
                <div class="gs_gray">J Verma, V Sharma, G Jain, NK Garg, V Shrivastava, P Garg</div>
                <div class="gs_gray">
                    2022 IEEE 10th Power India International Conference (PIICON)<span class="gs_oph">, 2023</span>
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=1749248769883335439"
                    class="gsc_a_ac gs_ibl"
                    >6</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2023</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=100&amp;pagesize=100&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:8d8msizDQcsC"
                    class="gsc_a_at"
                    >Probabilistic Load Flow Calculation using Method of Moments</a
                >
                <div class="gs_gray">MRB Shrivastava Vivek</div>
                <div class="gs_gray">
                    International Conference on Modelling &amp; Simulation (CITICOMS 2007)<span class="gs_oph"
                        >, 2007</span
                    >
                </div>
            </td>
            <td class="gsc_a_c"><a href="" class="gsc_a_ac gs_ibl"></a></td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2007</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=100&amp;pagesize=100&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:LO7wyVUgiFcC"
                    class="gsc_a_at"
                    >Probabilistic Load Flow Computation using Method of Moments &amp; Cumulants</a
                >
                <div class="gs_gray">RBM Vivek Shrivastava</div>
                <div class="gs_gray">
                    International Conference on Electrical Engineering design &amp; Technologies&nbsp;…<span
                        class="gs_oph"
                        >, 2007</span
                    >
                </div>
            </td>
            <td class="gsc_a_c"><a href="" class="gsc_a_ac gs_ibl"></a></td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2007</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=100&amp;pagesize=100&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:GtLg2Ama23sC"
                    class="gsc_a_at"
                    >Probabilistic Power System Planning using Bayesian Belief Networks</a
                >
                <div class="gs_gray">RBM Vivek Shrivastava</div>
                <div class="gs_gray">
                    Computational Intelligence to Emerging Electric Power Systems (CIEEPS’06&nbsp;…<span class="gs_oph"
                        >, 2006</span
                    >
                </div>
            </td>
            <td class="gsc_a_c"><a href="" class="gsc_a_ac gs_ibl"></a></td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2006</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=100&amp;pagesize=100&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:KbBQZpvPDL4C"
                    class="gsc_a_at"
                    >Probabilistic power system planning using soft computing methods</a
                >
                <div class="gs_gray">V Shrivastava</div>
                <div class="gs_gray">IIT Kharagpur<span class="gs_oph">, 2009</span></div>
            </td>
            <td class="gsc_a_c"><a href="" class="gsc_a_ac gs_ibl"></a></td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2009</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=100&amp;pagesize=100&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:PVjk1bu6vJQC"
                    class="gsc_a_at"
                    >Prognostics and health management of induction motor by supervised learning classifiers</a
                >
                <div class="gs_gray">R Jigyasu, V Shrivastava, S Singh</div>
                <div class="gs_gray">
                    IOP Conference Series: Materials Science and Engineering 1168 (1), 012006<span class="gs_oph"
                        >, 2021</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=18236128632632272653"
                    class="gsc_a_ac gs_ibl"
                    >12</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2021</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=100&amp;pagesize=100&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:3htObqc8RwsC"
                    class="gsc_a_at"
                    >Reliability Improvement of Distribution System by Optimal Sitting and Sizing of Disperse
                    Generation</a
                >
                <div class="gs_gray">VS Bhadoria, V Shrivastava, NS Pal, SP Jaiswal</div>
                <div class="gs_gray">
                    International Journal of Reliability, Quality and Safety Engineering 24 (6)<span class="gs_oph"
                        >, 2017</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=3712124134181498302,4708929579305138764"
                    class="gsc_a_ac gs_ibl"
                    >28</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2017</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=100&amp;pagesize=100&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:9pM33mqn1YgC"
                    class="gsc_a_at"
                    >Reliability Issues in a Deregulated Power System</a
                >
                <div class="gs_gray">S Vivek</div>
                <div class="gs_gray">
                    International Conference on Reliability and Safety Engineering (INCRESE 2005&nbsp;…<span
                        class="gs_oph"
                        >, 2005</span
                    >
                </div>
            </td>
            <td class="gsc_a_c"><a href="" class="gsc_a_ac gs_ibl"></a></td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2005</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=100&amp;pagesize=100&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:nZcligLrVowC"
                    class="gsc_a_at"
                    >Signals, Machines and Automation</a
                >
                <div class="gs_gray">A Rani, B Kumar, V Shrivastava, RC Bansal</div>
                <div class="gs_gray"></div>
            </td>
            <td class="gsc_a_c"><a href="" class="gsc_a_ac gs_ibl"></a></td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2023</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=100&amp;pagesize=100&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:HeT0ZceujKMC"
                    class="gsc_a_at"
                    >Signals, Machines and Automation: Select Proceedings of SIGMA 2022</a
                >
                <div class="gs_gray">A Rani, B Kumar, V Shrivastava, RC Bansal</div>
                <div class="gs_gray">Springer<span class="gs_oph">, 2023</span></div>
            </td>
            <td class="gsc_a_c"><a href="" class="gsc_a_ac gs_ibl"></a></td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2023</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=100&amp;pagesize=100&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:D_sINldO8mEC"
                    class="gsc_a_at"
                    >Simulation and modeling of a Constant voltage controller based solar powered water pumping
                    system</a
                >
                <div class="gs_gray">B Kumar, YK Chauhan, V Shrivastava</div>
                <div class="gs_gray">
                    International Conference on Heterogeneous Networking for Quality&nbsp;…<span class="gs_oph"
                        >, 2013</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=2279309252005105719"
                    class="gsc_a_ac gs_ibl"
                    >4</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2013</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=100&amp;pagesize=100&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:NXb4pA-qfm4C"
                    class="gsc_a_at"
                    >Single Phase Induction Motor Drive with Simplified FLC for Variable Speed Operations</a
                >
                <div class="gs_gray">SV Bhavnesh Kumar</div>
                <div class="gs_gray">
                    National Conference on Power and Energy Systems (NCPES 2011)<span class="gs_oph">, 2011</span>
                </div>
            </td>
            <td class="gsc_a_c"><a href="" class="gsc_a_ac gs_ibl"></a></td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2011</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=100&amp;pagesize=100&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:F9fV5C73w3QC"
                    class="gsc_a_at"
                    >Single Solution for Control and Synchronization of Inverters in Microgrids</a
                >
                <div class="gs_gray">S Bhambri, V Shrivastava, M Kumawat</div>
                <div class="gs_gray">
                    2023 9th IEEE India International Conference on Power Electronics (IICPE), 1-6<span class="gs_oph"
                        >, 2023</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=4044880467652075733"
                    class="gsc_a_ac gs_ibl"
                    >6</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2023</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=100&amp;pagesize=100&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:XoXfffV-tXoC"
                    class="gsc_a_at"
                    >Smart classifier based prognostics and health management of induction motor</a
                >
                <div class="gs_gray">R Jigyasu, V Shrivastava, S Singh</div>
                <div class="gs_gray">Materials Today: Proceedings 43, 355-361<span class="gs_oph">, 2021</span></div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=833137549362691823"
                    class="gsc_a_ac gs_ibl"
                    >22</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2021</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=100&amp;pagesize=100&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:8AbLer7MMksC"
                    class="gsc_a_at"
                    >Solar Powered Fuzzy Logic Controller based Vector Controlled Induction Motor Drive</a
                >
                <div class="gs_gray">B Kumar, YK Chauhan, V Shrivastava</div>
                <div class="gs_gray">
                    Journal of Automation and Control Engineering 1 (4)<span class="gs_oph">, 2013</span>
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=18183470592760949416"
                    class="gsc_a_ac gs_ibl"
                    >3</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2013</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=100&amp;pagesize=100&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:URolC5Kub84C"
                    class="gsc_a_at"
                    >Speed control of electric vehicle using fuzzy logic controller</a
                >
                <div class="gs_gray">S Agrawal, V Shrivastava</div>
                <div class="gs_gray">
                    2017 International Conference on Information, Communication, Instrumentation&nbsp;…<span
                        class="gs_oph"
                        >, 2017</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=3342198286673595850"
                    class="gsc_a_ac gs_ibl"
                    >10</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2017</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=100&amp;pagesize=100&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:r_AWSJRzSzQC"
                    class="gsc_a_at"
                    >Synchronization of UPFC in Active Distribution Systems</a
                >
                <div class="gs_gray">S pujan Jaiswal, V Shrivastava</div>
                <div class="gs_gray">Decision Analytics Applications in Industry<span class="gs_oph">, 0</span></div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=11556945739592972326"
                    class="gsc_a_ac gs_ibl"
                    >1</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl"></span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=100&amp;pagesize=100&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:e_rmSamDkqQC"
                    class="gsc_a_at"
                    >Synchronization of UPFC in Active Distribution Systems</a
                >
                <div class="gs_gray">SP Jaiswal, V Shrivastava</div>
                <div class="gs_gray">
                    Decision Analytics Applications in Industry, 37-49<span class="gs_oph">, 2020</span>
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=13408354906509905524"
                    class="gsc_a_ac gs_ibl"
                    >1</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2020</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=100&amp;pagesize=100&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:0CzhzZyukY4C"
                    class="gsc_a_at"
                    >Talo-calcaneal distraction Ilizarov frame: an ergonomic method to manage intra-articular fractures
                    of calcaneum</a
                >
                <div class="gs_gray">AR Singh, J Ahmad, VK Shrivastava, P Kumar</div>
                <div class="gs_gray">
                    Asian Journal of Medical Sciences 12 (7), 88-93<span class="gs_oph">, 2021</span>
                </div>
            </td>
            <td class="gsc_a_c"><a href="" class="gsc_a_ac gs_ibl"></a></td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2021</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=100&amp;pagesize=100&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:9Nmd_mFXekcC"
                    class="gsc_a_at"
                    >Technical analysis of solar pumping system based on irrigation requirement</a
                >
                <div class="gs_gray">G Dadhich, V Shrivastava</div>
                <div class="gs_gray">
                    2017 International Conference on Circuit, Power and Computing Technologies&nbsp;…<span
                        class="gs_oph"
                        >, 2017</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=1588501459320438229"
                    class="gsc_a_ac gs_ibl"
                    >4</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2017</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=100&amp;pagesize=100&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:FAceZFleit8C"
                    class="gsc_a_at"
                    >Test and Testability for VLSI Circuits</a
                >
                <div class="gs_gray">V Shrivastava</div>
                <div class="gs_gray">
                    Services through Information Technology Enabled Systems (SITES’03)<span class="gs_oph">, 2003</span>
                </div>
            </td>
            <td class="gsc_a_c"><a href="" class="gsc_a_ac gs_ibl"></a></td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2003</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=100&amp;pagesize=100&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:yMeIxYmEMEAC"
                    class="gsc_a_at"
                    >The Energy Mix: An Emerging Trend in Distribution System</a
                >
                <div class="gs_gray">S Bhambri, M Kumawat, V Shrivastava, U Agarwal, NK Jain</div>
                <div class="gs_gray">
                    Optimal Planning and Operation of Distributed Energy Resources, 11-37<span class="gs_oph"
                        >, 2023</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=14393495212801513017"
                    class="gsc_a_ac gs_ibl"
                    >10</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2023</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=100&amp;pagesize=100&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:WJVC3Jt7v1AC"
                    class="gsc_a_at"
                    >Transfer learning based bearing and rotor fault diagnosis of induction motor</a
                >
                <div class="gs_gray">R Jigyasu, V Shrivastava, S Singh, V Bhadoria</div>
                <div class="gs_gray">
                    2022 2nd International Conference on Advance Computing and Innovative&nbsp;…<span class="gs_oph"
                        >, 2022</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=3599011201936148517"
                    class="gsc_a_ac gs_ibl"
                    >14</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2022</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=100&amp;pagesize=100&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:anf4URPfarAC"
                    class="gsc_a_at"
                    >Two-Dimensional Warranty Analysis And Forecasting For Automotive Components</a
                >
                <div class="gs_gray">ST Shrivastava Vivek</div>
                <div class="gs_gray">
                    International Conference on Reliability &amp; Safety Engineering (INCRESE 2007)<span class="gs_oph"
                        >, 2007</span
                    >
                </div>
            </td>
            <td class="gsc_a_c"><a href="" class="gsc_a_ac gs_ibl"></a></td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2007</span></td>
        </tr>
        <tr class="gsc_a_tr">
            <td class="gsc_a_t">
                <a
                    href="/citations?view_op=view_citation&amp;hl=en&amp;user=xR0COBoAAAAJ&amp;cstart=100&amp;pagesize=100&amp;sortby=title&amp;citation_for_view=xR0COBoAAAAJ:AvfA0Oy_GE0C"
                    class="gsc_a_at"
                    >Viability of grid-connected solar PV system for a village of rajasthan</a
                >
                <div class="gs_gray">A Khandelwal, V Shrivastava</div>
                <div class="gs_gray">
                    2017 International Conference on Information, Communication, Instrumentation&nbsp;…<span
                        class="gs_oph"
                        >, 2017</span
                    >
                </div>
            </td>
            <td class="gsc_a_c">
                <a
                    href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=18343668215120484024"
                    class="gsc_a_ac gs_ibl"
                    >29</a
                >
            </td>
            <td class="gsc_a_y"><span class="gsc_a_h gsc_a_hc gs_ibl">2017</span></td>
        </tr>
    </tbody>
</table>

"""

from bs4 import BeautifulSoup
import json

soup = BeautifulSoup(html, "html.parser")

results = []

for row in soup.select("#gsc_a_t tbody tr"):
    title_el = row.select_one(".gsc_a_at")
    year_el = row.select_one(".gsc_a_y")

    if not title_el:
        continue

    year_text = year_el.get_text(strip=True) if year_el else ""

    results.append({
        "title": title_el.get_text(" ", strip=True),
        "year": int(year_text) if year_text.isdigit() else None,
        "link": title_el.get("href")
    })

with open("results.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)
