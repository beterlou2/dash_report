import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import pathlib

from dash.dependencies import Input, Output
from utils import make_dash_table

PATH = pathlib.Path(__file__)
DATA_PATH = PATH.joinpath("..\data").resolve()

stocks_asset = pd.read_csv(DATA_PATH.joinpath("stocks_asset.csv"))
accounting = pd.read_csv(DATA_PATH.joinpath("accounting.csv"))


app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
server = app.server

app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)


def create_layout(app):
    return html.Div(
        [
            #header(app),
            html.Div(
                [
                    "证券研究报告"
                ],
                className = "header",
            ),
    
            html.Div(
                [
                    html.Div(
                        [
                            html.Div(["公司研究/公告点评"], id = "title_part1",),
                            html.Div(["2020年06月07日"], id = "title_part2",),
                        ],
                        id = "title_left",
                    ),
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Div(["交运设备/汽车整车 II"], id = "title_part3",),
                                ],
                                id = "category",
                            ),
                        ],
                        id = "title_right",
                    ),
                ],
                className = "title",
            ),
            html.Div(
                [
                    html.Div(
                        [
                            html.Div(
                                [
                                   
                                    html.Div(
                                        [
                                           "投资评级：买入（维持评级）"
                                        ],
                                        className = "section_title",
                                    ),
                                    html.Div(
                                        [
                                        
                                            html.Div(
                                                [
                                                    html.P(["当前价格(元)："]),
                                                    html.P(["合理价格区间(元)： "]),
                                                ],
                                                id = "subsect1_left",
                                            ),
                                            html.Div(
                                                [
                                                    html.P(["18.23"]),
                                                    html.P(["24.64~26.40"]),
                                                ],
                                                id = "subsect1_right",
                                            ),
                                            html.Div([], id = "border_bot"),
                                            html.Div(
                                                [
                                                    html.Div(["林志轩"], className = "staff_name"),
                                                    html.Div(["研究员"], className = "staff_position"),
                                                    html.Div(["刘千琳"], className = "staff_name"),
                                                    html.Div(["研究员"], className = "staff_position"),
                                                    html.Div(["王涛"], className = "staff_name"),
                                                    html.Div(["研究员"], className = "staff_position"),
                                                    html.Div(["邢重阳"], className = "staff_name"),
                                                    html.Div(["联系人"], className = "staff_position"),
                                                ],
                                                id = "staff_info",
                                            ),
                                            html.Div(
                                                [
                                                    html.Div(
                                                        [
                                                            "执业证书编号：S0570519060005", 
                                                            html.Br(),
                                                            "021-28972090 ",
                                                            html.Br(),
                                                            "zhixuan.lin@htsc.com",
                                                        ], 
                                                        className = "contact_info",
                                                    ),
                                                    html.Div(
                                                        [
                                                            "执业证书编号：S0570518060004",
                                                            html.Br(),
                                                            "021-28972076",
                                                            html.Br(),
                                                            "liuqianlin@htsc.com",
                                                        ], 
                                                        className = "contact_info",
                                                    ),
                                                    html.Div(
                                                        [
                                                            "执业证书编号：S0570519110001",
                                                            html.Br(),
                                                            "021-28972053",
                                                            html.Br(),
                                                            "wangtao011711@htsc.com",
                                                        ], 
                                                        className = "contact_info",
                                                    ),
                                                    html.Div(
                                                        [
                                                            "021-38476205 ",
                                                            html.Br(),
                                                            "xingchongyang@htsc.com"
                                                        ], 
                                                        className = "contact_info",
                                                    ),
                                                ],
                                                id = "staff_contact",
                                            ),
                                        ],
                                        id = "subsect1",
                                    ),
                                ],
                                className = "block1",
                            ),
                           
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            "相关研究"
                                        ],
                                        className = "section_title",
                                    ),
                                    html.Div(
                                        [
                                            "1《上汽集团(600104 SH,买入): 19 盈利下滑 29%，龙头整装再出发》2020.01"
                                        ],
                                        className = "study_details",
                                    ),
                                    html.Div(
                                        [
                                            "2《上汽集团(600104 SH,买入): 产量同比提 升，批发销量跌幅收窄》2019.09"
                                        ],
                                        className = "study_details",
                                    ),
                                    html.Div(
                                        [
                                            "3《上汽集团(600104 SH,买入): Q2 终端折扣 大，业绩略低于预期》2019.08"
                                        ],
                                        className = "study_details",
                                    ),
                                ],
                                className = "block2",
                            ),
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            "一年股价走势图"
                                        ],
                                        className = "section_title",
                                    ),
                                    
                                    html.Div(
                                        [
                                            html.Img(src=app.get_asset_url('stocks.png')),
                                        ],
                                        className = "stocks_graph",
                                    ),
                                ],
                                className = "block3",
                            ),
                        ],
                        className = "col_left",
                    ),
                    html.Div(
                        [
                            html.Div(
                                [
                                "5月国内销量转正，上汽大众待改善"
                                   
                                ],
                                className = "cr_title",
                            ),
                            html.Div(
                                [
                                    "上汽集团(600104)"
                                ],
                                className = "cr_title2",
                            ),
                            html.Div(
                                [
                                    "5月国内销量增速转正，批发销量增速或弱于行业"
                                ],
                                className = "para_title",
                            ),
                            html.Div(
                                [
                                    "6月5日，公司发布5月销量情况。5月公司实现批发销量47.3万台，同比-1.6%，其中国内销量45.6万台，同比+0.3%。根据中汽协预测，5月汽车 销量同比+11%，上汽销量增速弱于行业，主要原因是受海外疫情影响，出口销量大幅下滑，同时上汽大众销量下滑。我们认为随着疫情结束，汽车需 求有望逐步恢复，Q2 汽车行业批发销量有望转正。随着行业恢复和公司战 略调整进一步深入，公司销量和归母净利润有望逐季恢复，预计 20-22 年 EPS 分别为 1.76、1.98、2.17 元，维持“买入”评级。"
                                ],
                                className = "para_body",
                            ),
                            html.P(),
                            html.Div(
                                [
                                    "上汽通用五菱销量改善明显，上汽通用、自主跌幅收窄"
                                ],
                                className = "para_title",
                            ),
                            html.Div(
                                [
                                    "5 月，上汽大众批发销量 13 万台，同比-15%，上汽通用批发销量 13.6 万 台，同比-3.6%，上汽自主批发销量 5.2 万台，同比-5%，上汽通用五菱批 发销量 12 万台，同比+11%；上汽大通销量 1.6 万台，同比+61%；上汽红 岩销量 10109 台，同比+110%。上汽集团开展了“五五”购物节促销活动， 商用车销量增长迅速，国内批发销量转正。上汽通用五菱战略转型后推出 了较多新车型，销量情况有明显改善。上汽通用三缸机车型逐步转回四缸 机，销量跌幅收窄。上汽自主新车 RX5 Plus 新车上市，销量跌幅收窄。细 分市场竞争激烈，上汽大众销量仍有下滑。"
                                ],
                                className = "para_body",
                            ),
                            html.P(),
                            html.Div(
                                [
                                    "上汽通用三缸机逐步转回四缸机，上汽自主 RX5 Plus 开启预售"
                                ],
                                className = "para_title",
                            ),
                            html.Div(
                                [
                                    "2019 年上汽通用批发销量同比-19%，其中一个原因是三缸机车型不受国 内消费者欢迎，上汽通用英朗、威朗等 13 个车型有三缸机版本。从 2020 年 4 月开始，上汽通用逐步将三缸机车型转回四缸，英朗和科鲁泽已经转 为四缸车型。5 月 4 日，RX5 Plus 开启预售，该车型是上汽自主主力车型 rx5 中期改款，新车共推出三个版本，官方预售价 12.28~13.98 万元。我 们认为新车在前脸设计、内饰设计和智能网联配置上有较大改善，RX5 Plus 有望帮助上汽自主提升 10~15 万紧凑型 SUV 细分领域市占率，上汽自主 销量有望逐季改善。"
                                ],
                                className = "para_body",
                            ),
                            html.P(),
                            html.Div(
                                [
                                    "销量和利润有望逐季改善，维持“买入”评级"
                                ],
                                className = "para_title",
                            ),
                            html.Div(
                                [
                                    "上汽通用和上汽通用五菱销量情况正在逐步改善。2020 年 Q4 上汽大众 MEB 工厂有望投产，上汽大众有望在新能源汽车领域取得突破。2021 年 上汽奥迪投产在望，公司进一步布局豪华车领域，未来发展值得期待。我 们预计公司 2020-22 年分别实现归母净利 205、231、254 亿元，EPS 分 别为 1.76、1.98、2.17 元，同行业可比公司 20 年平均估值 16.8XPE， 考虑到公司业绩弹性略弱于可比公司，维持公司 20 年 14~15XPE 估值， 维持目标价 24.64~26.4 元，维持“买入”评级。 "
                                ],
                                className = "para_body",
                            ),
                            html.P(),
                            html.Div(
                                [
                                    "风险提示：我国汽车销量增速不及预期，公司海外市场拓展不及预期。"
                                ],
                                className = "para_body",
                            ),
                        ],
                        className = "col_right",
                    ),
                    html.Div(
                        [
                            
                            html.Div(
                                [   
                                    html.Div(
                                        [
                                            "公司基本资料"
                                        ],
                                        className = "section_title",
                                    ),
                                    
                                    html.Div(
                                        [
                                            html.Table(make_dash_table(stocks_asset)),
                                        ],
                                        id = "table1",
                                    ),
                                ],
                                id = "block4",
                            ),
                            
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            "经营预测指标与估值"
                                        ],
                                        className = "section_title",
                                    ),
                                    html.Table(make_dash_table(accounting)),
                                ],
                                id = "block5",
                            ),
                        ],
                        className = "col_bot",
                    ),
                ],
                className = "body",
            ),
        ],
        className = "page",
    )

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])    
def display_page(pathname):
    return create_layout(app)
    
if __name__ == "__main__":
    app.run_server(debug=True)