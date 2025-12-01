# Copyright 2016-2018 Therp BV <https://therp.nl>.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).


def post_init_hook(env):
    pass
    # Depricated base.res_partner_title_madam not available anymore
    #gender_mappings = {
    #    "female": env.ref("base.res_partner_title_madam",raise_if_not_found=False)
    #    + env.ref("base.res_partner_title_miss", raise_if_not_found=False),
     #   "male": env.ref("base.res_partner_title_mister",raise_if_not_found=False),
    #}
    #for gender, titles in list(gender_mappings.items()):
    #    env["res.partner"].with_context(active_test=False).search(
    #        [("title", "in", titles.ids)]
    #    ).write({"gender": gender})
