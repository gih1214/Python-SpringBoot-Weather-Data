package site.gucci.weather.domain;

import javax.persistence.Entity;
import javax.persistence.Id;

import lombok.Data;

@Data
@Entity
public class Weather {

    @Id
    private Integer ID;

    private String MSRDT; // 측정일시
    private String MSRRGN_NM; // 권역명
    private String MSRSTE_NM; // 측정소명
    private String PM10; // 미세먼지
    private String PM25; // 초미세먼지농도
    private String O3; // 오존
    private String NO2; // 이산화질소농도
    private String CO; // 일산화탄소농도
    private String SO2; // 아황산가스농도
    private String IDEX_NM; // 통합대기환경등급
    private String IDEX_MVL; // 통합대기환경지수
    private String ARPLT_MAIN; // 지수결정물질
}
