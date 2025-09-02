import pandas as pd
from dash import Dash, dash_table, html

# 샘플 데이터
df = pd.DataFrame({
    "이름": ["홍길동", "김철수", "이영희", "박민수"],
    "나이": [30, 25, 41, 37],
    "직무": ["데이터분석", "백엔드", "PM", "프론트엔드"],
    "입사일": pd.to_datetime(["2021-01-02", "2020-05-10", "2019-03-20", "2022-07-01"])
})

app = Dash(__name__)
app.title = "DataFrame Grid"

app.layout = html.Div([
    html.H3("사원 테이블"),
    dash_table.DataTable(
        id="tbl",
        data=df.to_dict("records"),
        columns=[
            {"name": "이름", "id": "이름"},
            {"name": "나이", "id": "나이", "type": "numeric"},
            {"name": "직무", "id": "직무", "presentation": "dropdown"},
            {"name": "입사일", "id": "입사일", "type": "datetime"}
        ],
        editable=True,                 # 셀 편집
        filter_action="native",        # 필터
        sort_action="native",          # 정렬
        page_size=10,                  # 페이지네이션
        dropdown={                     # 드롭다운 편집(직무)
            "직무": {
                "options": [{"label": v, "value": v} for v in df["직무"].unique()]
            }
        },
        style_table={"height": "500px", "overflowY": "auto"},
        style_header={"fontWeight": "bold"},
        style_cell={"minWidth": 80, "maxWidth": 250, "whiteSpace": "normal"},
    )
])

if __name__ == "__main__":
    app.run(debug=True)

