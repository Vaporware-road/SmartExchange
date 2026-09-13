/**
 * Which Vue component draws which catalog entry.
 *
 * Written out rather than globbed so the mapping is greppable from both
 * sides: `website/tests.py::CatalogIntegrityTests` reads this file and fails
 * the build if the catalog offers a layout or a variant nothing here can
 * draw. A blank section on a customer's live site is not an acceptable way
 * to find that out.
 *
 * Imports are eager on purpose. A published site is one page and the whole
 * set is small; forty-two separate chunks would cost a visitor forty-two
 * round trips to render one screen.
 */
import ChromeOnepage from './layouts/Onepage.vue'
import ChromeSidebar from './layouts/Sidebar.vue'
import ChromeSplit from './layouts/Split.vue'
import ChromeStandard from './layouts/Standard.vue'
import AboutTextImage from './sections/about/TextImage.vue'
import AboutColumns from './sections/about/Columns.vue'
import AboutStatement from './sections/about/Statement.vue'
import ContactSplitMap from './sections/contact/SplitMap.vue'
import ContactCards from './sections/contact/Cards.vue'
import ContactForm from './sections/contact/Form.vue'
import CtaBanner from './sections/cta/Banner.vue'
import CtaBoxed from './sections/cta/Boxed.vue'
import CtaGradient from './sections/cta/Gradient.vue'
import FaqAccordion from './sections/faq/Accordion.vue'
import FaqTwoColumn from './sections/faq/TwoColumn.vue'
import FeaturesGrid from './sections/features/Grid.vue'
import FeaturesAlternating from './sections/features/Alternating.vue'
import FeaturesBento from './sections/features/Bento.vue'
import FooterSimple from './sections/footer/Simple.vue'
import FooterColumns from './sections/footer/Columns.vue'
import FooterRich from './sections/footer/Rich.vue'
import GalleryMasonry from './sections/gallery/Masonry.vue'
import GalleryCarousel from './sections/gallery/Carousel.vue'
import HeaderMinimal from './sections/header/Minimal.vue'
import HeaderCentered from './sections/header/Centered.vue'
import HeaderFloating from './sections/header/Floating.vue'
import HeaderSplit from './sections/header/Split.vue'
import HeroSplitImage from './sections/hero/SplitImage.vue'
import HeroCentered from './sections/hero/Centered.vue'
import HeroFullBleed from './sections/hero/FullBleed.vue'
import HeroRatesFirst from './sections/hero/RatesFirst.vue'
import HeroStacked from './sections/hero/Stacked.vue'
import RatesCards from './sections/rates/Cards.vue'
import RatesTable from './sections/rates/Table.vue'
import RatesTicker from './sections/rates/Ticker.vue'
import RatesGrid from './sections/rates/Grid.vue'
import RatesFeatured from './sections/rates/Featured.vue'
import ServicesIconGrid from './sections/services/IconGrid.vue'
import ServicesCards from './sections/services/Cards.vue'
import ServicesList from './sections/services/List.vue'
import StatsBar from './sections/stats/Bar.vue'
import StatsCards from './sections/stats/Cards.vue'
import StepsTimeline from './sections/steps/Timeline.vue'
import StepsNumberedCards from './sections/steps/NumberedCards.vue'
import TestimonialsSlider from './sections/testimonials/Slider.vue'
import TestimonialsGrid from './sections/testimonials/Grid.vue'

/** `<section type>/<variant>` from the catalog to the component that draws it. */
const SECTIONS = {
  'about/text-image': AboutTextImage,
  'about/columns': AboutColumns,
  'about/statement': AboutStatement,
  'contact/split-map': ContactSplitMap,
  'contact/cards': ContactCards,
  'contact/form': ContactForm,
  'cta/banner': CtaBanner,
  'cta/boxed': CtaBoxed,
  'cta/gradient': CtaGradient,
  'faq/accordion': FaqAccordion,
  'faq/two-column': FaqTwoColumn,
  'features/grid': FeaturesGrid,
  'features/alternating': FeaturesAlternating,
  'features/bento': FeaturesBento,
  'footer/simple': FooterSimple,
  'footer/columns': FooterColumns,
  'footer/rich': FooterRich,
  'gallery/masonry': GalleryMasonry,
  'gallery/carousel': GalleryCarousel,
  'header/minimal': HeaderMinimal,
  'header/centered': HeaderCentered,
  'header/floating': HeaderFloating,
  'header/split': HeaderSplit,
  'hero/split-image': HeroSplitImage,
  'hero/centered': HeroCentered,
  'hero/full-bleed': HeroFullBleed,
  'hero/rates-first': HeroRatesFirst,
  'hero/stacked': HeroStacked,
  'rates/cards': RatesCards,
  'rates/table': RatesTable,
  'rates/ticker': RatesTicker,
  'rates/grid': RatesGrid,
  'rates/featured': RatesFeatured,
  'services/icon-grid': ServicesIconGrid,
  'services/cards': ServicesCards,
  'services/list': ServicesList,
  'stats/bar': StatsBar,
  'stats/cards': StatsCards,
  'steps/timeline': StepsTimeline,
  'steps/numbered-cards': StepsNumberedCards,
  'testimonials/slider': TestimonialsSlider,
  'testimonials/grid': TestimonialsGrid,
}

/** Page chrome: how a layout arranges its sections, not how they look. */
const CHROMES = {
  onepage: ChromeOnepage,
  sidebar: ChromeSidebar,
  split: ChromeSplit,
  standard: ChromeStandard,
}

/**
 * Every layout in the catalog, mapped to the chrome it renders with.
 * Listed by slug so a future layout can claim bespoke chrome without the
 * catalog having to know which component file that is.
 */
const LAYOUTS = {
  'aurora': 'standard',
  'ledger': 'standard',
  'bazaar': 'standard',
  'vault': 'standard',
  'pulse': 'onepage',
  'atlas': 'standard',
  'prism': 'standard',
  'harbor': 'sidebar',
  'quartz': 'standard',
  'meridian': 'split',
}

/** The component for a section, or null when the catalog and this file disagree. */
export function sectionComponent(type, variant) {
  return SECTIONS[`${type}/${variant}`] || null
}

/** The chrome a layout renders with, falling back to the plain stacked page. */
export function layoutComponent(layoutSlug, chrome) {
  return CHROMES[chrome || LAYOUTS[layoutSlug]] || CHROMES.standard
}

export { SECTIONS, CHROMES, LAYOUTS }
