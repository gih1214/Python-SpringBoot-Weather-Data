package site.gucci.weather.web;

import java.util.List;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import lombok.RequiredArgsConstructor;
import site.gucci.weather.domain.Weather;
import site.gucci.weather.domain.WeatherRepository;

@RequiredArgsConstructor
@Controller
public class WeatherController {

    private final WeatherRepository weatherRepository;

    @GetMapping("/")
    public String list(Model model) {
        List<Weather> weatherEntity = weatherRepository.findAll();
        model.addAttribute("weather", weatherEntity);
        return "/list";
    }
}
