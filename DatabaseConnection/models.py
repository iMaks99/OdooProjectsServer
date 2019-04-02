from django.db import models


class BaseImportImport(models.Model):
    res_model = models.CharField(max_length=1000, blank=True, null=True)
    file = models.BinaryField(blank=True, null=True)
    file_name = models.CharField(max_length=1000, blank=True, null=True)
    file_type = models.CharField(max_length=1000, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='BaseImportImport_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='BaseImportImport_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_import'


class BaseImportMapping(models.Model):
    res_model = models.CharField(max_length=5000, blank=True, null=True)
    column_name = models.CharField(max_length=5000, blank=True, null=True)
    field_name = models.CharField(max_length=5000, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='BaseImportMapping_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='BaseImportMapping_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_mapping'


class BaseImportTestsModelsChar(models.Model):
    value = models.CharField(max_length=1000, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='BaseImportTestsModelsChar_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='BaseImportTestsModelsChar_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char'


class BaseImportTestsModelsCharNoreadonly(models.Model):
    value = models.CharField(max_length=1000, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING,
                                   related_name='BaseImportTestsModelsCharNoreadonly_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING,
                                  related_name='BaseImportTestsModelsCharNoreadonly_write_uid', db_column='write_uid',
                                  blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char_noreadonly'


class BaseImportTestsModelsCharReadonly(models.Model):
    value = models.CharField(max_length=1000, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING,
                                   related_name='BaseImportTestsModelsCharReadonly_create_uid', db_column='create_uid',
                                   blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING,
                                  related_name='BaseImportTestsModelsCharReadonly_write_uid', db_column='write_uid',
                                  blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char_readonly'


class BaseImportTestsModelsCharRequired(models.Model):
    value = models.CharField(max_length=1000)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING,
                                   related_name='BaseImportTestsModelsCharRequired_create_uid', db_column='create_uid',
                                   blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING,
                                  related_name='BaseImportTestsModelsCharRequired_write_uid', db_column='write_uid',
                                  blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char_required'


class BaseImportTestsModelsCharStates(models.Model):
    value = models.CharField(max_length=1000, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING,
                                   related_name='BaseImportTestsModelsCharStates_create_uid', db_column='create_uid',
                                   blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING,
                                  related_name='BaseImportTestsModelsCharStates_write_uid', db_column='write_uid',
                                  blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char_states'


class BaseImportTestsModelsCharStillreadonly(models.Model):
    value = models.CharField(max_length=1000, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING,
                                   related_name='BaseImportTestsModelsCharStillreadonly_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING,
                                  related_name='BaseImportTestsModelsCharStillreadonly_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char_stillreadonly'


class BaseImportTestsModelsComplex(models.Model):
    f = models.FloatField(blank=True, null=True)
    m = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    c = models.CharField(max_length=1000, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, related_name='BaseImportTestsModelsComplex_currency',
                                 blank=True, null=True)
    d = models.DateField(blank=True, null=True)
    dt = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING,
                                   related_name='BaseImportTestsModelsComplex_create_uid', db_column='create_uid',
                                   blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='BaseImportTestsModelsComplex_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_complex'


class BaseImportTestsModelsFloat(models.Model):
    value = models.FloatField(blank=True, null=True)
    value2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, related_name='BaseImportTestsModelsFloat_currency',
                                 blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='BaseImportTestsModelsFloat_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='BaseImportTestsModelsFloat_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_float'


class BaseImportTestsModelsM2O(models.Model):
    value = models.ForeignKey('BaseImportTestsModelsM2ORelated', models.DO_NOTHING,
                              related_name='BaseImportTestsModelsM2O_value', db_column='value', blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='BaseImportTestsModelsM2O_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='BaseImportTestsModelsM2O_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_m2o'


class BaseImportTestsModelsM2ORelated(models.Model):
    value = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING,
                                   related_name='BaseImportTestsModelsM2ORelated_create_uid', db_column='create_uid',
                                   blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING,
                                  related_name='BaseImportTestsModelsM2ORelated_write_uid', db_column='write_uid',
                                  blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_m2o_related'


class BaseImportTestsModelsM2ORequired(models.Model):
    value = models.ForeignKey('BaseImportTestsModelsM2ORequiredRelated', models.DO_NOTHING,
                              related_name='BaseImportTestsModelsM2ORequired_value', db_column='value')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING,
                                   related_name='BaseImportTestsModelsM2ORequired_create_uid', db_column='create_uid',
                                   blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING,
                                  related_name='BaseImportTestsModelsM2ORequired_write_uid', db_column='write_uid',
                                  blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_m2o_required'


class BaseImportTestsModelsM2ORequiredRelated(models.Model):
    value = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING,
                                   related_name='BaseImportTestsModelsM2ORequiredRelated_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING,
                                  related_name='BaseImportTestsModelsM2ORequiredRelated_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_m2o_required_related'


class BaseImportTestsModelsO2M(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='BaseImportTestsModelsO2M_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='BaseImportTestsModelsO2M_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_o2m'


class BaseImportTestsModelsO2MChild(models.Model):
    parent = models.ForeignKey(BaseImportTestsModelsO2M, models.DO_NOTHING,
                               related_name='BaseImportTestsModelsO2MChild_parent', blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING,
                                   related_name='BaseImportTestsModelsO2MChild_create_uid', db_column='create_uid',
                                   blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='BaseImportTestsModelsO2MChild_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_o2m_child'


class BaseImportTestsModelsPreview(models.Model):
    name = models.CharField(max_length=1000, blank=True, null=True)
    somevalue = models.IntegerField()
    othervalue = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING,
                                   related_name='BaseImportTestsModelsPreview_create_uid', db_column='create_uid',
                                   blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='BaseImportTestsModelsPreview_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_preview'


class BaseLanguageExport(models.Model):
    name = models.CharField(max_length=1000, blank=True, null=True)
    lang = models.CharField(max_length=1000)
    format = models.CharField(max_length=1000)
    data = models.BinaryField(blank=True, null=True)
    state = models.CharField(max_length=1000, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='BaseLanguageExport_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='BaseLanguageExport_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_language_export'


class BaseLanguageImport(models.Model):
    name = models.CharField(max_length=1000)
    code = models.CharField(max_length=5)
    data = models.BinaryField()
    filename = models.CharField(max_length=1000)
    overwrite = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='BaseLanguageImport_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='BaseLanguageImport_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_language_import'


class BaseLanguageInstall(models.Model):
    lang = models.CharField(max_length=1000)
    overwrite = models.BooleanField(blank=True, null=True)
    state = models.CharField(max_length=1000, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='BaseLanguageInstall_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='BaseLanguageInstall_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_language_install'


class BaseModuleUninstall(models.Model):
    show_all = models.BooleanField(blank=True, null=True)
    module = models.ForeignKey('IrModuleModule', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='BaseModuleUninstall_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='BaseModuleUninstall_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_module_uninstall'


class BaseModuleUpdate(models.Model):
    updated = models.IntegerField(blank=True, null=True)
    added = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=1000, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='BaseModuleUpdate_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='BaseModuleUpdate_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_module_update'


class BaseModuleUpgrade(models.Model):
    module_info = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='BaseModuleUpgrade_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='BaseModuleUpgrade_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_module_upgrade'


class BasePartnerMergeAutomaticWizard(models.Model):
    group_by_email = models.BooleanField(blank=True, null=True)
    group_by_name = models.BooleanField(blank=True, null=True)
    group_by_is_company = models.BooleanField(blank=True, null=True)
    group_by_vat = models.BooleanField(blank=True, null=True)
    group_by_parent_id = models.BooleanField(blank=True, null=True)
    state = models.CharField(max_length=1000)
    number_group = models.IntegerField(blank=True, null=True)
    current_line = models.ForeignKey('BasePartnerMergeLine', models.DO_NOTHING,
                                     related_name='BasePartnerMergeAutomaticWizard_current_line', blank=True, null=True)
    dst_partner = models.ForeignKey('ResPartner', models.DO_NOTHING,
                                    related_name='BasePartnerMergeAutomaticWizard_dst_partner', blank=True, null=True)
    exclude_contact = models.BooleanField(blank=True, null=True)
    exclude_journal_item = models.BooleanField(blank=True, null=True)
    maximum_group = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING,
                                   related_name='BasePartnerMergeAutomaticWizard_create_uid', db_column='create_uid',
                                   blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING,
                                  related_name='BasePartnerMergeAutomaticWizard_write_uid', db_column='write_uid',
                                  blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_partner_merge_automatic_wizard'


class BasePartnerMergeAutomaticWizardResPartnerRel(models.Model):
    base_partner_merge_automatic_wizard = models.ForeignKey(BasePartnerMergeAutomaticWizard, models.DO_NOTHING)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'base_partner_merge_automatic_wizard_res_partner_rel'
        unique_together = (('base_partner_merge_automatic_wizard', 'res_partner'),)


class BasePartnerMergeLine(models.Model):
    wizard = models.ForeignKey(BasePartnerMergeAutomaticWizard, models.DO_NOTHING,
                               related_name='BasePartnerMergeLine_wizard', blank=True, null=True)
    min_id = models.IntegerField(blank=True, null=True)
    aggr_ids = models.CharField(max_length=1000)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='BasePartnerMergeLine_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='BasePartnerMergeLine_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_partner_merge_line'


class BaseUpdateTranslations(models.Model):
    lang = models.CharField(max_length=1000)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='BaseUpdateTranslations_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='BaseUpdateTranslations_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_update_translations'


class BusBus(models.Model):
    channel = models.CharField(max_length=1000, blank=True, null=True)
    message = models.CharField(max_length=1000, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='BusBus_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='BusBus_write_uid', db_column='write_uid',
                                  blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bus_bus'


class BusPresence(models.Model):
    user = models.OneToOneField('ResUsers', models.DO_NOTHING, related_name='BusPresence_user')
    last_poll = models.DateTimeField(blank=True, null=True)
    last_presence = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bus_presence'


class CalendarAlarm(models.Model):
    name = models.CharField(max_length=1000)
    type = models.CharField(max_length=1000)
    duration = models.IntegerField()
    interval = models.CharField(max_length=1000)
    duration_minutes = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='CalendarAlarm_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='CalendarAlarm_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calendar_alarm'


class CalendarAlarmCalendarEventRel(models.Model):
    calendar_event = models.ForeignKey('CalendarEvent', models.DO_NOTHING)
    calendar_alarm = models.ForeignKey(CalendarAlarm, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'calendar_alarm_calendar_event_rel'
        unique_together = (('calendar_event', 'calendar_alarm'),)


class CalendarAttendee(models.Model):
    state = models.CharField(max_length=1000, blank=True, null=True)
    common_name = models.CharField(max_length=1000, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name='CalendarAttendee_partner', blank=True,
                                null=True)
    email = models.CharField(max_length=1000, blank=True, null=True)
    availability = models.CharField(max_length=1000, blank=True, null=True)
    access_token = models.CharField(max_length=1000, blank=True, null=True)
    event = models.ForeignKey('CalendarEvent', models.DO_NOTHING, related_name='CalendarAttendee_event', blank=True,
                              null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='CalendarAttendee_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='CalendarAttendee_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calendar_attendee'


class CalendarContacts(models.Model):
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='CalendarContacts_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='CalendarContacts_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calendar_contacts'
        unique_together = (('user', 'partner'),)


class CalendarEvent(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING,
                                                related_name='CalendarEvent_message_main_attachment', blank=True,
                                                null=True)
    name = models.CharField(max_length=1000)
    state = models.CharField(max_length=1000, blank=True, null=True)
    display_start = models.CharField(max_length=1000, blank=True, null=True)
    start = models.DateTimeField()
    stop = models.DateTimeField()
    allday = models.BooleanField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    start_datetime = models.DateTimeField(blank=True, null=True)
    stop_date = models.DateField(blank=True, null=True)
    stop_datetime = models.DateTimeField(blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    privacy = models.CharField(max_length=1000, blank=True, null=True)
    location = models.CharField(max_length=1000, blank=True, null=True)
    show_as = models.CharField(max_length=1000, blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)
    res_model = models.ForeignKey('IrModel', models.DO_NOTHING, related_name='CalendarEvent_res_model', blank=True,
                                  null=True)
    res_model_0 = models.CharField(db_column='res_model', max_length=1000, blank=True,
                                   null=True)  # Field renamed because of name conflict.
    rrule = models.CharField(max_length=1000, blank=True, null=True)
    rrule_type = models.CharField(max_length=1000, blank=True, null=True)
    recurrency = models.BooleanField(blank=True, null=True)
    recurrent_id = models.IntegerField(blank=True, null=True)
    recurrent_id_date = models.DateTimeField(blank=True, null=True)
    end_type = models.CharField(max_length=1000, blank=True, null=True)
    interval = models.IntegerField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    mo = models.BooleanField(blank=True, null=True)
    tu = models.BooleanField(blank=True, null=True)
    we = models.BooleanField(blank=True, null=True)
    th = models.BooleanField(blank=True, null=True)
    fr = models.BooleanField(blank=True, null=True)
    sa = models.BooleanField(blank=True, null=True)
    su = models.BooleanField(blank=True, null=True)
    month_by = models.CharField(max_length=1000, blank=True, null=True)
    day = models.IntegerField(blank=True, null=True)
    week_list = models.CharField(max_length=1000, blank=True, null=True)
    byday = models.CharField(max_length=1000, blank=True, null=True)
    final_date = models.DateField(blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='CalendarEvent_user', blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='CalendarEvent_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='CalendarEvent_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    opportunity = models.ForeignKey('CrmLead', models.DO_NOTHING, related_name='CalendarEvent_opportunity', blank=True,
                                    null=True)

    class Meta:
        managed = False
        db_table = 'calendar_event'


class CalendarEventResPartnerRel(models.Model):
    calendar_event = models.ForeignKey(CalendarEvent, models.DO_NOTHING)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'calendar_event_res_partner_rel'
        unique_together = (('calendar_event', 'res_partner'),)


class CalendarEventType(models.Model):
    name = models.CharField(unique=True, max_length=1000)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='CalendarEventType_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='CalendarEventType_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calendar_event_type'


class ChangePasswordUser(models.Model):
    wizard = models.ForeignKey('ChangePasswordWizard', models.DO_NOTHING)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)
    user_login = models.CharField(max_length=1000, blank=True, null=True)
    new_passwd = models.CharField(max_length=1000, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ChangePasswordUser_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ChangePasswordUser_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'change_password_user'


class ChangePasswordWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ChangePasswordWizard_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ChangePasswordWizard_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'change_password_wizard'


class CrmLead(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING,
                                                related_name='CrmLead_message_main_attachment', blank=True, null=True)
    campaign = models.ForeignKey('UtmCampaign', models.DO_NOTHING, related_name='CrmLead_campaign', blank=True,
                                 null=True)
    source = models.ForeignKey('UtmSource', models.DO_NOTHING, related_name='CrmLead_source', blank=True, null=True)
    medium = models.ForeignKey('UtmMedium', models.DO_NOTHING, related_name='CrmLead_medium', blank=True, null=True)
    name = models.CharField(max_length=1000)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name='CrmLead_partner', blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    date_action_last = models.DateTimeField(blank=True, null=True)
    email_from = models.CharField(max_length=1000, blank=True, null=True)
    website = models.CharField(max_length=1000, blank=True, null=True)
    team = models.ForeignKey('CrmTeam', models.DO_NOTHING, related_name='CrmLead_team', blank=True, null=True)
    email_cc = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    contact_name = models.CharField(max_length=1000, blank=True, null=True)
    partner_name = models.CharField(max_length=1000, blank=True, null=True)
    type = models.CharField(max_length=1000)
    priority = models.CharField(max_length=1000, blank=True, null=True)
    date_closed = models.DateTimeField(blank=True, null=True)
    stage = models.ForeignKey('CrmStage', models.DO_NOTHING, related_name='CrmLead_stage', blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='CrmLead_user', blank=True, null=True)
    referred = models.CharField(max_length=1000, blank=True, null=True)
    date_open = models.DateTimeField(blank=True, null=True)
    day_open = models.FloatField(blank=True, null=True)
    day_close = models.FloatField(blank=True, null=True)
    date_last_stage_update = models.DateTimeField(blank=True, null=True)
    date_conversion = models.DateTimeField(blank=True, null=True)
    message_bounce = models.IntegerField(blank=True, null=True)
    probability = models.FloatField(blank=True, null=True)
    planned_revenue = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    expected_revenue = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    date_deadline = models.DateField(blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    street = models.CharField(max_length=1000, blank=True, null=True)
    street2 = models.CharField(max_length=1000, blank=True, null=True)
    zip = models.CharField(max_length=1000, blank=True, null=True)
    city = models.CharField(max_length=1000, blank=True, null=True)
    state = models.ForeignKey('ResCountryState', models.DO_NOTHING, related_name='CrmLead_state', blank=True, null=True)
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, related_name='CrmLead_country', blank=True, null=True)
    phone = models.CharField(max_length=1000, blank=True, null=True)
    mobile = models.CharField(max_length=1000, blank=True, null=True)
    function = models.CharField(max_length=1000, blank=True, null=True)
    title = models.ForeignKey('ResPartnerTitle', models.DO_NOTHING, related_name='CrmLead_title', db_column='title',
                              blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name='CrmLead_company', blank=True, null=True)
    lost_reason = models.ForeignKey('CrmLostReason', models.DO_NOTHING, related_name='CrmLead_lost_reason',
                                    db_column='lost_reason', blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='CrmLead_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='CrmLead_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_lead'


class CrmLead2OpportunityPartner(models.Model):
    name = models.CharField(max_length=1000)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='CrmLead2OpportunityPartner_user', blank=True,
                             null=True)
    team = models.ForeignKey('CrmTeam', models.DO_NOTHING, related_name='CrmLead2OpportunityPartner_team', blank=True,
                             null=True)
    action = models.CharField(max_length=1000)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name='CrmLead2OpportunityPartner_partner',
                                blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='CrmLead2OpportunityPartner_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='CrmLead2OpportunityPartner_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_lead2opportunity_partner'


class CrmLead2OpportunityPartnerMass(models.Model):
    team = models.ForeignKey('CrmTeam', models.DO_NOTHING, related_name='CrmLead2OpportunityPartnerMass_team',
                             blank=True, null=True)
    deduplicate = models.BooleanField(blank=True, null=True)
    action = models.CharField(max_length=1000)
    force_assignation = models.BooleanField(blank=True, null=True)
    name = models.CharField(max_length=1000)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='CrmLead2OpportunityPartnerMass_user',
                             blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name='CrmLead2OpportunityPartnerMass_partner',
                                blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING,
                                   related_name='CrmLead2OpportunityPartnerMass_create_uid', db_column='create_uid',
                                   blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING,
                                  related_name='CrmLead2OpportunityPartnerMass_write_uid', db_column='write_uid',
                                  blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_lead2opportunity_partner_mass'


class CrmLead2OpportunityPartnerMassResUsersRel(models.Model):
    crm_lead2opportunity_partner_mass = models.ForeignKey(CrmLead2OpportunityPartnerMass, models.DO_NOTHING)
    res_users = models.ForeignKey('ResUsers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'crm_lead2opportunity_partner_mass_res_users_rel'
        unique_together = (('crm_lead2opportunity_partner_mass', 'res_users'),)


class CrmLeadCrmLead2OpportunityPartnerMassRel(models.Model):
    crm_lead2opportunity_partner_mass = models.ForeignKey(CrmLead2OpportunityPartnerMass, models.DO_NOTHING)
    crm_lead = models.ForeignKey(CrmLead, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'crm_lead_crm_lead2opportunity_partner_mass_rel'
        unique_together = (('crm_lead2opportunity_partner_mass', 'crm_lead'),)


class CrmLeadCrmLead2OpportunityPartnerRel(models.Model):
    crm_lead2opportunity_partner = models.ForeignKey(CrmLead2OpportunityPartner, models.DO_NOTHING)
    crm_lead = models.ForeignKey(CrmLead, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'crm_lead_crm_lead2opportunity_partner_rel'
        unique_together = (('crm_lead2opportunity_partner', 'crm_lead'),)


class CrmLeadLost(models.Model):
    lost_reason = models.ForeignKey('CrmLostReason', models.DO_NOTHING, related_name='CrmLeadLost_lost_reason',
                                    blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='CrmLeadLost_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='CrmLeadLost_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_lead_lost'


class CrmLeadTag(models.Model):
    name = models.CharField(unique=True, max_length=1000)
    color = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='CrmLeadTag_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='CrmLeadTag_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_lead_tag'


class CrmLeadTagRel(models.Model):
    lead = models.ForeignKey(CrmLead, models.DO_NOTHING)
    tag = models.ForeignKey(CrmLeadTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'crm_lead_tag_rel'
        unique_together = (('lead', 'tag'),)


class CrmLostReason(models.Model):
    name = models.CharField(max_length=1000)
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='CrmLostReason_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='CrmLostReason_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_lost_reason'


class CrmMergeOpportunity(models.Model):
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='CrmMergeOpportunity_user', blank=True,
                             null=True)
    team = models.ForeignKey('CrmTeam', models.DO_NOTHING, related_name='CrmMergeOpportunity_team', blank=True,
                             null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='CrmMergeOpportunity_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='CrmMergeOpportunity_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_merge_opportunity'


class CrmPartnerBinding(models.Model):
    action = models.CharField(max_length=1000)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name='CrmPartnerBinding_partner', blank=True,
                                null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='CrmPartnerBinding_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='CrmPartnerBinding_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_partner_binding'


class CrmStage(models.Model):
    name = models.CharField(max_length=1000)
    sequence = models.IntegerField(blank=True, null=True)
    probability = models.FloatField()
    on_change = models.BooleanField(blank=True, null=True)
    requirements = models.TextField(blank=True, null=True)
    team = models.ForeignKey('CrmTeam', models.DO_NOTHING, related_name='CrmStage_team', blank=True, null=True)
    legend_priority = models.TextField(blank=True, null=True)
    fold = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='CrmStage_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='CrmStage_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_stage'


class CrmTeam(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING,
                                                related_name='CrmTeam_message_main_attachment', blank=True, null=True)
    name = models.CharField(max_length=1000)
    active = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name='CrmTeam_company', blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='CrmTeam_user', blank=True, null=True)
    reply_to = models.CharField(max_length=1000, blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    team_type = models.CharField(max_length=1000)
    dashboard_graph_model = models.CharField(max_length=1000, blank=True, null=True)
    dashboard_graph_group = models.CharField(max_length=1000, blank=True, null=True)
    dashboard_graph_period = models.CharField(max_length=1000, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='CrmTeam_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='CrmTeam_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    use_leads = models.BooleanField(blank=True, null=True)
    use_opportunities = models.BooleanField(blank=True, null=True)
    alias = models.ForeignKey('MailAlias', models.DO_NOTHING)
    dashboard_graph_group_pipeline = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_team'


class DigestDigest(models.Model):
    name = models.CharField(max_length=1000)
    periodicity = models.CharField(max_length=1000)
    next_run_date = models.DateField(blank=True, null=True)
    template = models.ForeignKey('MailTemplate', models.DO_NOTHING)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name='DigestDigest_company', blank=True,
                                null=True)
    state = models.CharField(max_length=1000, blank=True, null=True)
    kpi_res_users_connected = models.BooleanField(blank=True, null=True)
    kpi_mail_message_total = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='DigestDigest_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='DigestDigest_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    kpi_project_task_opened = models.BooleanField(blank=True, null=True)
    kpi_crm_lead_created = models.BooleanField(blank=True, null=True)
    kpi_crm_opportunities_won = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'digest_digest'


class DigestDigestResUsersRel(models.Model):
    digest_digest = models.ForeignKey(DigestDigest, models.DO_NOTHING)
    res_users = models.ForeignKey('ResUsers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'digest_digest_res_users_rel'
        unique_together = (('digest_digest', 'res_users'),)


class DigestTip(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    tip_description = models.TextField(blank=True, null=True)
    group = models.ForeignKey('ResGroups', models.DO_NOTHING, related_name='DigestTip_group', blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='DigestTip_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='DigestTip_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'digest_tip'


class DigestTipResUsersRel(models.Model):
    digest_tip = models.ForeignKey(DigestTip, models.DO_NOTHING)
    res_users = models.ForeignKey('ResUsers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'digest_tip_res_users_rel'
        unique_together = (('digest_tip', 'res_users'),)


class EmailTemplateAttachmentRel(models.Model):
    email_template = models.ForeignKey('MailTemplate', models.DO_NOTHING)
    attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'email_template_attachment_rel'
        unique_together = (('email_template', 'attachment'),)


class EmailTemplatePreview(models.Model):
    res_id = models.CharField(max_length=1000, blank=True, null=True)
    name = models.CharField(max_length=1000, blank=True, null=True)
    model = models.ForeignKey('IrModel', models.DO_NOTHING, related_name='EmailTemplatePreview_model', blank=True,
                              null=True)
    model_0 = models.CharField(db_column='model', max_length=1000, blank=True,
                               null=True)  # Field renamed because of name conflict.
    lang = models.CharField(max_length=1000, blank=True, null=True)
    user_signature = models.BooleanField(blank=True, null=True)
    subject = models.CharField(max_length=1000, blank=True, null=True)
    email_from = models.CharField(max_length=1000, blank=True, null=True)
    use_default_to = models.BooleanField(blank=True, null=True)
    email_to = models.CharField(max_length=1000, blank=True, null=True)
    partner_to = models.CharField(max_length=1000, blank=True, null=True)
    email_cc = models.CharField(max_length=1000, blank=True, null=True)
    reply_to = models.CharField(max_length=1000, blank=True, null=True)
    mail_server = models.ForeignKey('IrMailServer', models.DO_NOTHING, related_name='EmailTemplatePreview_mail_server',
                                    blank=True, null=True)
    body_html = models.TextField(blank=True, null=True)
    report_name = models.CharField(max_length=1000, blank=True, null=True)
    report_template = models.ForeignKey('IrActReportXml', models.DO_NOTHING,
                                        related_name='EmailTemplatePreview_report_template',
                                        db_column='report_template', blank=True, null=True)
    ref_ir_act_window = models.ForeignKey('IrActWindow', models.DO_NOTHING,
                                          related_name='EmailTemplatePreview_ref_ir_act_window',
                                          db_column='ref_ir_act_window', blank=True, null=True)
    auto_delete = models.BooleanField(blank=True, null=True)
    model_object_field = models.ForeignKey('IrModelFields', models.DO_NOTHING,
                                           related_name='EmailTemplatePreview_model_object_field',
                                           db_column='model_object_field', blank=True, null=True)
    sub_object = models.ForeignKey('IrModel', models.DO_NOTHING, related_name='EmailTemplatePreview_sub_object',
                                   db_column='sub_object', blank=True, null=True)
    sub_model_object_field = models.ForeignKey('IrModelFields', models.DO_NOTHING,
                                               related_name='EmailTemplatePreview_sub_model_object_field',
                                               db_column='sub_model_object_field', blank=True, null=True)
    null_value = models.CharField(max_length=1000, blank=True, null=True)
    copyvalue = models.CharField(max_length=1000, blank=True, null=True)
    scheduled_date = models.CharField(max_length=1000, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='EmailTemplatePreview_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='EmailTemplatePreview_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_template_preview'


class EmailTemplatePreviewResPartnerRel(models.Model):
    email_template_preview = models.ForeignKey(EmailTemplatePreview, models.DO_NOTHING)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'email_template_preview_res_partner_rel'
        unique_together = (('email_template_preview', 'res_partner'),)


class EmployeeCategoryRel(models.Model):
    category = models.ForeignKey('HrEmployeeCategory', models.DO_NOTHING)
    emp = models.ForeignKey('HrEmployee', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'employee_category_rel'
        unique_together = (('category', 'emp'),)


class FetchmailServer(models.Model):
    name = models.CharField(max_length=1000)
    active = models.BooleanField(blank=True, null=True)
    state = models.CharField(max_length=1000, blank=True, null=True)
    server = models.CharField(max_length=1000, blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=1000)
    is_ssl = models.BooleanField(blank=True, null=True)
    attach = models.BooleanField(blank=True, null=True)
    original = models.BooleanField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    user = models.CharField(max_length=1000, blank=True, null=True)
    password = models.CharField(max_length=1000, blank=True, null=True)
    object = models.ForeignKey('IrModel', models.DO_NOTHING, related_name='FetchmailServer_object', blank=True,
                               null=True)
    priority = models.IntegerField(blank=True, null=True)
    configuration = models.TextField(blank=True, null=True)
    script = models.CharField(max_length=1000, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='FetchmailServer_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='FetchmailServer_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fetchmail_server'


class HrDepartment(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING,
                                                related_name='HrDepartment_message_main_attachment', blank=True,
                                                null=True)
    name = models.CharField(max_length=1000)
    complete_name = models.CharField(max_length=1000, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name='HrDepartment_company', blank=True,
                                null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, related_name='HrDepartment_parent', blank=True, null=True)
    manager = models.ForeignKey('HrEmployee', models.DO_NOTHING, related_name='HrDepartment_manager', blank=True,
                                null=True)
    note = models.TextField(blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='HrDepartment_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='HrDepartment_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_department'


class HrDepartmentMailChannelRel(models.Model):
    mail_channel = models.ForeignKey('MailChannel', models.DO_NOTHING)
    hr_department = models.ForeignKey(HrDepartment, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hr_department_mail_channel_rel'
        unique_together = (('mail_channel', 'hr_department'),)


class HrEmployee(models.Model):
    resource = models.ForeignKey('ResourceResource', models.DO_NOTHING)
    message_main_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING,
                                                related_name='HrEmployee_message_main_attachment', blank=True,
                                                null=True)
    name = models.CharField(max_length=1000, blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='HrEmployee_user', blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    address_home = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name='HrEmployee_address_home',
                                     blank=True, null=True)
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, related_name='HrEmployee_country', blank=True,
                                null=True)
    gender = models.CharField(max_length=1000, blank=True, null=True)
    marital = models.CharField(max_length=1000, blank=True, null=True)
    spouse_complete_name = models.CharField(max_length=1000, blank=True, null=True)
    spouse_birthdate = models.DateField(blank=True, null=True)
    children = models.IntegerField(blank=True, null=True)
    place_of_birth = models.CharField(max_length=1000, blank=True, null=True)
    country_of_birth = models.ForeignKey('ResCountry', models.DO_NOTHING, related_name='HrEmployee_country_of_birth',
                                         db_column='country_of_birth', blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    ssnid = models.CharField(max_length=1000, blank=True, null=True)
    sinid = models.CharField(max_length=1000, blank=True, null=True)
    identification_id = models.CharField(max_length=1000, blank=True, null=True)
    passport_id = models.CharField(max_length=1000, blank=True, null=True)
    bank_account = models.ForeignKey('ResPartnerBank', models.DO_NOTHING, related_name='HrEmployee_bank_account',
                                     blank=True, null=True)
    permit_no = models.CharField(max_length=1000, blank=True, null=True)
    visa_no = models.CharField(max_length=1000, blank=True, null=True)
    visa_expire = models.DateField(blank=True, null=True)
    additional_note = models.TextField(blank=True, null=True)
    certificate = models.CharField(max_length=1000, blank=True, null=True)
    study_field = models.CharField(max_length=1000, blank=True, null=True)
    study_school = models.CharField(max_length=1000, blank=True, null=True)
    emergency_contact = models.CharField(max_length=1000, blank=True, null=True)
    emergency_phone = models.CharField(max_length=1000, blank=True, null=True)
    km_home_work = models.IntegerField(blank=True, null=True)
    google_drive_link = models.CharField(max_length=1000, blank=True, null=True)
    job_title = models.CharField(max_length=1000, blank=True, null=True)
    address = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name='HrEmployee_address', blank=True,
                                null=True)
    work_phone = models.CharField(max_length=1000, blank=True, null=True)
    mobile_phone = models.CharField(max_length=1000, blank=True, null=True)
    work_email = models.CharField(max_length=1000, blank=True, null=True)
    work_location = models.CharField(max_length=1000, blank=True, null=True)
    job = models.ForeignKey('HrJob', models.DO_NOTHING, related_name='HrEmployee_job', blank=True, null=True)
    department = models.ForeignKey(HrDepartment, models.DO_NOTHING, related_name='HrEmployee_department', blank=True,
                                   null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, related_name='HrEmployee_parent', blank=True, null=True)
    coach = models.ForeignKey('self', models.DO_NOTHING, related_name='HrEmployee_coach', blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name='HrEmployee_company', blank=True,
                                null=True)
    resource_calendar = models.ForeignKey('ResourceCalendar', models.DO_NOTHING,
                                          related_name='HrEmployee_resource_calendar', blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='HrEmployee_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='HrEmployee_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_employee'


class HrEmployeeCategory(models.Model):
    name = models.CharField(unique=True, max_length=1000)
    color = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='HrEmployeeCategory_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='HrEmployeeCategory_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_employee_category'


class HrJob(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING,
                                                related_name='HrJob_message_main_attachment', blank=True, null=True)
    name = models.CharField(max_length=1000)
    expected_employees = models.IntegerField(blank=True, null=True)
    no_of_employee = models.IntegerField(blank=True, null=True)
    no_of_recruitment = models.IntegerField(blank=True, null=True)
    no_of_hired_employee = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    requirements = models.TextField(blank=True, null=True)
    department = models.ForeignKey(HrDepartment, models.DO_NOTHING, related_name='HrJob_department', blank=True,
                                   null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name='HrJob_company', blank=True, null=True)
    state = models.CharField(max_length=1000)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='HrJob_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='HrJob_write_uid', db_column='write_uid',
                                  blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_job'
        unique_together = (('name', 'company', 'department'),)


class IapAccount(models.Model):
    service_name = models.CharField(max_length=1000, blank=True, null=True)
    account_token = models.CharField(max_length=1000, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name='IapAccount_company', blank=True,
                                null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IapAccount_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IapAccount_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iap_account'


class IrActClient(models.Model):
    name = models.CharField(max_length=1000)
    type = models.CharField(max_length=1000)
    help = models.TextField(blank=True, null=True)
    binding_model = models.ForeignKey('IrModel', models.DO_NOTHING, related_name='IrActClient_binding_model',
                                      blank=True, null=True)
    binding_type = models.CharField(max_length=1000)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrActClient_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrActClient_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    tag = models.CharField(max_length=1000)
    target = models.CharField(max_length=1000, blank=True, null=True)
    res_model = models.CharField(max_length=1000, blank=True, null=True)
    context = models.CharField(max_length=1000)
    params_store = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_act_client'


class IrActReportXml(models.Model):
    name = models.CharField(max_length=1000)
    type = models.CharField(max_length=1000)
    help = models.TextField(blank=True, null=True)
    binding_model = models.ForeignKey('IrModel', models.DO_NOTHING, related_name='IrActReportXml_binding_model',
                                      blank=True, null=True)
    binding_type = models.CharField(max_length=1000)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrActReportXml_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrActReportXml_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    model = models.CharField(max_length=1000)
    report_type = models.CharField(max_length=1000)
    report_name = models.CharField(max_length=1000)
    report_file = models.CharField(max_length=1000, blank=True, null=True)
    multi = models.BooleanField(blank=True, null=True)
    paperformat = models.ForeignKey('ReportPaperformat', models.DO_NOTHING, related_name='IrActReportXml_paperformat',
                                    blank=True, null=True)
    print_report_name = models.CharField(max_length=1000, blank=True, null=True)
    attachment_use = models.BooleanField(blank=True, null=True)
    attachment = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_act_report_xml'


class IrActServer(models.Model):
    name = models.CharField(max_length=1000)
    type = models.CharField(max_length=1000)
    help = models.TextField(blank=True, null=True)
    binding_model = models.ForeignKey('IrModel', models.DO_NOTHING, related_name='IrActServer_binding_model',
                                      blank=True, null=True)
    binding_type = models.CharField(max_length=1000)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrActServer_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrActServer_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    usage = models.CharField(max_length=1000)
    state = models.CharField(max_length=1000)
    sequence = models.IntegerField(blank=True, null=True)
    model = models.ForeignKey('IrModel', models.DO_NOTHING)
    model_name = models.CharField(max_length=1000, blank=True, null=True)
    code = models.TextField(blank=True, null=True)
    crud_model = models.ForeignKey('IrModel', models.DO_NOTHING, related_name='IrActServer_crud_model', blank=True,
                                   null=True)
    link_field = models.ForeignKey('IrModelFields', models.DO_NOTHING, related_name='IrActServer_link_filed',
                                   blank=True, null=True)
    template = models.ForeignKey('MailTemplate', models.DO_NOTHING, related_name='IrActServer_template', blank=True,
                                 null=True)
    activity_type = models.ForeignKey('MailActivityType', models.DO_NOTHING, related_name='IrActServer_activity_type',
                                      blank=True, null=True)
    activity_summary = models.CharField(max_length=1000, blank=True, null=True)
    activity_note = models.TextField(blank=True, null=True)
    activity_date_deadline_range = models.IntegerField(blank=True, null=True)
    activity_date_deadline_range_type = models.CharField(max_length=1000, blank=True, null=True)
    activity_user_type = models.CharField(max_length=1000)
    activity_user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrActServer_activity_user',
                                      blank=True, null=True)
    activity_user_field_name = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_act_server'


class IrActServerMailChannelRel(models.Model):
    ir_act_server = models.ForeignKey(IrActServer, models.DO_NOTHING)
    mail_channel = models.ForeignKey('MailChannel', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ir_act_server_mail_channel_rel'
        unique_together = (('ir_act_server', 'mail_channel'),)


class IrActServerResPartnerRel(models.Model):
    ir_act_server = models.ForeignKey(IrActServer, models.DO_NOTHING)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ir_act_server_res_partner_rel'
        unique_together = (('ir_act_server', 'res_partner'),)


class IrActUrl(models.Model):
    name = models.CharField(max_length=1000)
    type = models.CharField(max_length=1000)
    help = models.TextField(blank=True, null=True)
    binding_model = models.ForeignKey('IrModel', models.DO_NOTHING, related_name='IrActUrl_binding_model', blank=True,
                                      null=True)
    binding_type = models.CharField(max_length=1000)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrActUrl_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrActUrl_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    url = models.TextField()
    target = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'ir_act_url'


class IrActWindow(models.Model):
    name = models.CharField(max_length=1000)
    type = models.CharField(max_length=1000)
    help = models.TextField(blank=True, null=True)
    binding_model = models.ForeignKey('IrModel', models.DO_NOTHING, related_name='IrActWindow_binding_model',
                                      blank=True, null=True)
    binding_type = models.CharField(max_length=1000)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrActWindow_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrActWindow_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    view = models.ForeignKey('IrUiView', models.DO_NOTHING, related_name='IrActWindow_view', blank=True, null=True)
    domain = models.CharField(max_length=1000, blank=True, null=True)
    context = models.CharField(max_length=1000)
    res_id = models.IntegerField(blank=True, null=True)
    res_model = models.CharField(max_length=1000)
    src_model = models.CharField(max_length=1000, blank=True, null=True)
    target = models.CharField(max_length=1000, blank=True, null=True)
    view_mode = models.CharField(max_length=1000)
    view_type = models.CharField(max_length=1000)
    usage = models.CharField(max_length=1000, blank=True, null=True)
    limit = models.IntegerField(blank=True, null=True)
    search_view = models.ForeignKey('IrUiView', models.DO_NOTHING, related_name='IrActWindow_search_view', blank=True,
                                    null=True)
    filter = models.BooleanField(blank=True, null=True)
    auto_search = models.BooleanField(blank=True, null=True)
    multi = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_act_window'


class IrActWindowGroupRel(models.Model):
    act = models.ForeignKey(IrActWindow, models.DO_NOTHING)
    gid = models.ForeignKey('ResGroups', models.DO_NOTHING, related_name='IrActWindowGroupRel_gid', db_column='gid')

    class Meta:
        managed = False
        db_table = 'ir_act_window_group_rel'
        unique_together = (('act', 'gid'),)


class IrActWindowView(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    view = models.ForeignKey('IrUiView', models.DO_NOTHING, related_name='IrActWindowView_view', blank=True, null=True)
    view_mode = models.CharField(max_length=1000)
    act_window = models.ForeignKey(IrActWindow, models.DO_NOTHING, related_name='IrActWindowView_act_window',
                                   blank=True, null=True)
    multi = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrActWindowView_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrActWindowView_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_act_window_view'
        unique_together = (('act_window', 'view_mode'),)


class IrActions(models.Model):
    name = models.CharField(max_length=1000)
    type = models.CharField(max_length=1000)
    help = models.TextField(blank=True, null=True)
    binding_model = models.ForeignKey('IrModel', models.DO_NOTHING, related_name='IrActions_binding_model', blank=True,
                                      null=True)
    binding_type = models.CharField(max_length=1000)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrActions_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrActions_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_actions'


class IrActionsTodo(models.Model):
    action_id = models.IntegerField()
    sequence = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrActionsTodo_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrActionsTodo_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_actions_todo'


class IrAttachment(models.Model):
    name = models.CharField(max_length=1000)
    datas_fname = models.CharField(max_length=1000, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    res_name = models.CharField(max_length=1000, blank=True, null=True)
    res_model = models.CharField(max_length=1000, blank=True, null=True)
    res_model_name = models.CharField(max_length=1000, blank=True, null=True)
    res_field = models.CharField(max_length=1000, blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name='IrAttachment_company', blank=True,
                                null=True)
    type = models.CharField(max_length=1000)
    url = models.CharField(max_length=1024, blank=True, null=True)
    public = models.BooleanField(blank=True, null=True)
    access_token = models.CharField(max_length=1000, blank=True, null=True)
    db_datas = models.BinaryField(blank=True, null=True)
    store_fname = models.CharField(max_length=1000, blank=True, null=True)
    file_size = models.IntegerField(blank=True, null=True)
    checksum = models.CharField(max_length=40, blank=True, null=True)
    mimetype = models.CharField(max_length=1000, blank=True, null=True)
    index_content = models.TextField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrAttachment_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrAttachment_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_attachment'


class IrConfigParameter(models.Model):
    key = models.CharField(unique=True, max_length=1000)
    value = models.TextField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrConfigParameter_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrConfigParameter_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_config_parameter'


class IrCron(models.Model):
    ir_actions_server = models.ForeignKey(IrActServer, models.DO_NOTHING)
    cron_name = models.CharField(max_length=1000, blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)
    active = models.BooleanField(blank=True, null=True)
    interval_number = models.IntegerField(blank=True, null=True)
    interval_type = models.CharField(max_length=1000, blank=True, null=True)
    numbercall = models.IntegerField(blank=True, null=True)
    doall = models.BooleanField(blank=True, null=True)
    nextcall = models.DateTimeField()
    priority = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrCron_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrCron_write_uid', db_column='write_uid',
                                  blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_cron'


class IrDefault(models.Model):
    field = models.ForeignKey('IrModelFields', models.DO_NOTHING)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrDefault_user', blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name='IrDefault_company', blank=True,
                                null=True)
    condition = models.CharField(max_length=1000, blank=True, null=True)
    json_value = models.CharField(max_length=1000)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrDefault_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrDefault_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_default'


class IrDemo(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrDemo_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrDemo_write_uid', db_column='write_uid',
                                  blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_demo'


class IrDemoFailure(models.Model):
    module = models.ForeignKey('IrModuleModule', models.DO_NOTHING)
    error = models.CharField(max_length=1000, blank=True, null=True)
    wizard = models.ForeignKey('IrDemoFailureWizard', models.DO_NOTHING, related_name='IrDemoFailure_wizard',
                               blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrDemoFailure_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrDemoFailure_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_demo_failure'


class IrDemoFailureWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrDemoFailureWizard_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrDemoFailureWizard_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_demo_failure_wizard'


class IrExports(models.Model):
    name = models.CharField(max_length=1000, blank=True, null=True)
    resource = models.CharField(max_length=1000, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrExports_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrExports_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_exports'


class IrExportsLine(models.Model):
    name = models.CharField(max_length=1000, blank=True, null=True)
    export = models.ForeignKey(IrExports, models.DO_NOTHING, related_name='IrExportsLine', blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrExportsLine_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrExportsLine_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_exports_line'


class IrFilters(models.Model):
    name = models.CharField(max_length=1000)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrFilters_uesr', blank=True, null=True)
    domain = models.TextField()
    context = models.TextField()
    sort = models.TextField()
    model_id = models.CharField(max_length=1000)
    is_default = models.BooleanField(blank=True, null=True)
    action_id = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrFilters_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrFilters_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    # A unique constraint could not be introspected.
    class Meta:
        managed = False
        db_table = 'ir_filters'
        unique_together = (('name', 'model_id', 'user', 'action_id'),)


class IrLogging(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    create_uid = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=1000)
    type = models.CharField(max_length=1000)
    dbname = models.CharField(max_length=1000, blank=True, null=True)
    level = models.CharField(max_length=1000, blank=True, null=True)
    message = models.TextField()
    path = models.CharField(max_length=1000)
    func = models.CharField(max_length=1000)
    line = models.CharField(max_length=1000)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrLogging_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_logging'


class IrMailServer(models.Model):
    name = models.CharField(max_length=1000)
    smtp_host = models.CharField(max_length=1000)
    smtp_port = models.IntegerField()
    smtp_user = models.CharField(max_length=1000, blank=True, null=True)
    smtp_pass = models.CharField(max_length=1000, blank=True, null=True)
    smtp_encryption = models.CharField(max_length=1000)
    smtp_debug = models.BooleanField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrMailServer_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrMailServer_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_mail_server'


class IrModel(models.Model):
    name = models.CharField(max_length=1000)
    model = models.CharField(unique=True, max_length=1000)
    info = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=1000, blank=True, null=True)
    transient = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrModel_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrModel_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    is_mail_thread = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_model'


class IrModelAccess(models.Model):
    name = models.CharField(max_length=1000)
    active = models.BooleanField(blank=True, null=True)
    model = models.ForeignKey(IrModel, models.DO_NOTHING)
    group = models.ForeignKey('ResGroups', models.DO_NOTHING, related_name='IrModelAccess_group', blank=True, null=True)
    perm_read = models.BooleanField(blank=True, null=True)
    perm_write = models.BooleanField(blank=True, null=True)
    perm_create = models.BooleanField(blank=True, null=True)
    perm_unlink = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrModelAccess_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrModelAccess_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_model_access'


class IrModelConstraint(models.Model):
    name = models.CharField(max_length=1000)
    definition = models.CharField(max_length=1000, blank=True, null=True)
    model = models.ForeignKey(IrModel, models.DO_NOTHING, related_name='IrModelConstraint_model', db_column='model')
    module = models.ForeignKey('IrModuleModule', models.DO_NOTHING, related_name='IrModelConstraint_module',
                               db_column='module')
    type = models.CharField(max_length=1)
    date_update = models.DateTimeField(blank=True, null=True)
    date_init = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrModelConstraint_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrModelConstraint_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_model_constraint'
        unique_together = (('name', 'module'),)


class IrModelData(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrModelData_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrModelData_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    noupdate = models.BooleanField(blank=True, null=True)
    name = models.CharField(max_length=1000)
    date_init = models.DateTimeField(blank=True, null=True)
    date_update = models.DateTimeField(blank=True, null=True)
    module = models.CharField(max_length=1000)
    model = models.CharField(max_length=1000)
    res_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_model_data'
        unique_together = (('module', 'name'),)


class IrModelFields(models.Model):
    name = models.CharField(max_length=1000)
    complete_name = models.CharField(max_length=1000, blank=True, null=True)
    model = models.CharField(max_length=1000)
    relation = models.CharField(max_length=1000, blank=True, null=True)
    relation_field = models.CharField(max_length=1000, blank=True, null=True)
    relation_field_0 = models.ForeignKey('self', models.DO_NOTHING, related_name='IrModelFields_relation_field_0',
                                         db_column='relation_field_id', blank=True,
                                         null=True)  # Field renamed because of name conflict.
    model_0 = models.ForeignKey(IrModel, models.DO_NOTHING, related_name='IrModelFields_model_0',
                                db_column='model_id')  # Field renamed because of name conflict.
    field_description = models.CharField(max_length=1000)
    help = models.TextField(blank=True, null=True)
    ttype = models.CharField(max_length=1000)
    selection = models.CharField(max_length=1000, blank=True, null=True)
    copied = models.BooleanField(blank=True, null=True)
    related = models.CharField(max_length=1000, blank=True, null=True)
    related_field = models.ForeignKey('self', models.DO_NOTHING, related_name='IrModelFields_related_field', blank=True,
                                      null=True)
    required = models.BooleanField(blank=True, null=True)
    readonly = models.BooleanField(blank=True, null=True)
    index = models.BooleanField(blank=True, null=True)
    translate = models.BooleanField(blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=1000)
    on_delete = models.CharField(max_length=1000, blank=True, null=True)
    domain = models.CharField(max_length=1000, blank=True, null=True)
    selectable = models.BooleanField(blank=True, null=True)
    relation_table = models.CharField(max_length=1000, blank=True, null=True)
    column1 = models.CharField(max_length=1000, blank=True, null=True)
    column2 = models.CharField(max_length=1000, blank=True, null=True)
    compute = models.TextField(blank=True, null=True)
    depends = models.CharField(max_length=1000, blank=True, null=True)
    store = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrModelFields_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrModelFields_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    track_visibility = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_model_fields'
        unique_together = (('model', 'name'),)


class IrModelFieldsGroupRel(models.Model):
    field = models.ForeignKey(IrModelFields, models.DO_NOTHING)
    group = models.ForeignKey('ResGroups', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ir_model_fields_group_rel'
        unique_together = (('field', 'group'),)


class IrModelRelation(models.Model):
    name = models.CharField(max_length=1000)
    model = models.ForeignKey(IrModel, models.DO_NOTHING, related_name='IrModelRelation_model', db_column='model')
    module = models.ForeignKey('IrModuleModule', models.DO_NOTHING, related_name='IrModelRelation_module',
                               db_column='module')
    date_update = models.DateTimeField(blank=True, null=True)
    date_init = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrModelRelation_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrModelRelation_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_model_relation'


class IrModuleCategory(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrModuleCategory_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrModuleCategory_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, related_name='IrModuleCategory_parent', blank=True, null=True)
    name = models.CharField(max_length=1000)
    description = models.TextField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    visible = models.BooleanField(blank=True, null=True)
    exclusive = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_module_category'


class IrModuleModule(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrModuleModule_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrModuleModule_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    website = models.CharField(max_length=1000, blank=True, null=True)
    summary = models.CharField(max_length=1000, blank=True, null=True)
    name = models.CharField(unique=True, max_length=1000)
    author = models.CharField(max_length=1000, blank=True, null=True)
    icon = models.CharField(max_length=1000, blank=True, null=True)
    state = models.CharField(max_length=16, blank=True, null=True)
    latest_version = models.CharField(max_length=1000, blank=True, null=True)
    shortdesc = models.CharField(max_length=1000, blank=True, null=True)
    category = models.ForeignKey(IrModuleCategory, models.DO_NOTHING, related_name='IrModuleModule_category',
                                 blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    application = models.BooleanField(blank=True, null=True)
    demo = models.BooleanField(blank=True, null=True)
    web = models.BooleanField(blank=True, null=True)
    license = models.CharField(max_length=32, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    auto_install = models.BooleanField(blank=True, null=True)
    to_buy = models.BooleanField(blank=True, null=True)
    maintainer = models.CharField(max_length=1000, blank=True, null=True)
    contributors = models.TextField(blank=True, null=True)
    published_version = models.CharField(max_length=1000, blank=True, null=True)
    url = models.CharField(max_length=1000, blank=True, null=True)
    menus_by_module = models.TextField(blank=True, null=True)
    reports_by_module = models.TextField(blank=True, null=True)
    views_by_module = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_module_module'


class IrModuleModuleDependency(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrModuleModuleDependency_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrModuleModuleDependency_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=1000, blank=True, null=True)
    module = models.ForeignKey(IrModuleModule, models.DO_NOTHING, related_name='IrModuleModuleDependency_module',
                               blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_module_module_dependency'


class IrModuleModuleExclusion(models.Model):
    name = models.CharField(max_length=1000, blank=True, null=True)
    module = models.ForeignKey(IrModuleModule, models.DO_NOTHING, related_name='IrModuleModuleExclusion_module',
                               blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrModuleModuleExclusion_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrModuleModuleExclusion_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_module_module_exclusion'


class IrProperty(models.Model):
    name = models.CharField(max_length=1000, blank=True, null=True)
    res_id = models.CharField(max_length=1000, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name='IrProperty_company', blank=True,
                                null=True)
    fields = models.ForeignKey(IrModelFields, models.DO_NOTHING)
    value_float = models.FloatField(blank=True, null=True)
    value_integer = models.IntegerField(blank=True, null=True)
    value_text = models.TextField(blank=True, null=True)
    value_binary = models.BinaryField(blank=True, null=True)
    value_reference = models.CharField(max_length=1000, blank=True, null=True)
    value_datetime = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=1000)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrProperty_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrProperty_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_property'


class IrRule(models.Model):
    name = models.CharField(max_length=1000, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    model = models.ForeignKey(IrModel, models.DO_NOTHING)
    domain_force = models.TextField(blank=True, null=True)
    perm_read = models.BooleanField(blank=True, null=True)
    perm_write = models.BooleanField(blank=True, null=True)
    perm_create = models.BooleanField(blank=True, null=True)
    perm_unlink = models.BooleanField(blank=True, null=True)
    global_field = models.BooleanField(db_column='global', blank=True,
                                       null=True)  # Field renamed because it was a Python reserved word.
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrRule_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrRule_write_uid', db_column='write_uid',
                                  blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_rule'


class IrSequence(models.Model):
    name = models.CharField(max_length=1000)
    code = models.CharField(max_length=1000, blank=True, null=True)
    implementation = models.CharField(max_length=1000)
    active = models.BooleanField(blank=True, null=True)
    prefix = models.CharField(max_length=1000, blank=True, null=True)
    suffix = models.CharField(max_length=1000, blank=True, null=True)
    number_next = models.IntegerField()
    number_increment = models.IntegerField()
    padding = models.IntegerField()
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name='IrSequence_company', blank=True,
                                null=True)
    use_date_range = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrSequence_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrSequence_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_sequence'


class IrSequenceDateRange(models.Model):
    date_from = models.DateField()
    date_to = models.DateField()
    sequence = models.ForeignKey(IrSequence, models.DO_NOTHING)
    number_next = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrSequenceDateRange_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrSequenceDateRange_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_sequence_date_range'


class IrServerObjectLines(models.Model):
    server = models.ForeignKey(IrActServer, models.DO_NOTHING, related_name='IrServerObjectLines_server', blank=True,
                               null=True)
    col1 = models.ForeignKey(IrModelFields, models.DO_NOTHING, related_name='IrServerObjectLines_coll',
                             db_column='col1')
    value = models.TextField()
    type = models.CharField(max_length=1000)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrServerObjectLines_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrServerObjectLines_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_server_object_lines'


class IrTranslation(models.Model):
    name = models.CharField(max_length=1000)
    res_id = models.IntegerField(blank=True, null=True)
    lang = models.ForeignKey('ResLang', models.DO_NOTHING, related_name='IrTranslation_lang', db_column='lang',
                             blank=True, null=True)
    type = models.CharField(max_length=1000, blank=True, null=True)
    src = models.TextField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    module = models.CharField(max_length=1000, blank=True, null=True)
    state = models.CharField(max_length=1000, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)

    # A unique constraint could not be introspected.
    class Meta:
        managed = False
        db_table = 'ir_translation'
        unique_together = (('type', 'lang'), ('type', 'lang', 'name', 'res_id'), ('type', 'lang', 'name'),
                           ('type', 'name', 'lang', 'res_id'),)


class IrUiMenu(models.Model):
    parent_path = models.CharField(max_length=1000, blank=True, null=True)
    name = models.CharField(max_length=1000)
    active = models.BooleanField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, related_name='IrUiMenu_parent', blank=True, null=True)
    web_icon = models.CharField(max_length=1000, blank=True, null=True)
    action = models.CharField(max_length=1000, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrUiMenu_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrUiMenu_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_ui_menu'


class IrUiMenuGroupRel(models.Model):
    menu = models.ForeignKey(IrUiMenu, models.DO_NOTHING)
    gid = models.ForeignKey('ResGroups', models.DO_NOTHING, related_name='IrUiMenuGroupRel_gid', db_column='gid')

    class Meta:
        managed = False
        db_table = 'ir_ui_menu_group_rel'
        unique_together = (('menu', 'gid'),)


class IrUiView(models.Model):
    name = models.CharField(max_length=1000)
    model = models.CharField(max_length=1000, blank=True, null=True)
    key = models.CharField(max_length=1000, blank=True, null=True)
    priority = models.IntegerField()
    type = models.CharField(max_length=1000, blank=True, null=True)
    arch_db = models.TextField(blank=True, null=True)
    arch_fs = models.CharField(max_length=1000, blank=True, null=True)
    inherit = models.ForeignKey('self', models.DO_NOTHING, related_name='IrUiView_inherit', blank=True, null=True)
    field_parent = models.CharField(max_length=1000, blank=True, null=True)
    mode = models.CharField(max_length=1000)
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrUiView_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrUiView_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_ui_view'


class IrUiViewCustom(models.Model):
    ref = models.ForeignKey(IrUiView, models.DO_NOTHING)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)
    arch = models.TextField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrUiViewCustom_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='IrUiViewCustom_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_ui_view_custom'


class IrUiViewGroupRel(models.Model):
    view = models.ForeignKey(IrUiView, models.DO_NOTHING)
    group = models.ForeignKey('ResGroups', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ir_ui_view_group_rel'
        unique_together = (('view', 'group'),)


class MailActivity(models.Model):
    res_id = models.IntegerField()
    res_model = models.ForeignKey(IrModel, models.DO_NOTHING)
    res_model_0 = models.CharField(db_column='res_model', max_length=1000, blank=True,
                                   null=True)  # Field renamed because of name conflict.
    res_name = models.CharField(max_length=1000, blank=True, null=True)
    activity_type = models.ForeignKey('MailActivityType', models.DO_NOTHING, related_name='MailActivity_activity_type',
                                      blank=True, null=True)
    summary = models.CharField(max_length=1000, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)
    date_deadline = models.DateField()
    automated = models.BooleanField(blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)
    create_user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='MailActivity_create_user', blank=True,
                                    null=True)
    recommended_activity_type = models.ForeignKey('MailActivityType', models.DO_NOTHING,
                                                  related_name='MailActivity_recommended_activity_type', blank=True,
                                                  null=True)
    previous_activity_type = models.ForeignKey('MailActivityType', models.DO_NOTHING,
                                               related_name='MailActivity_previous_activity_type', blank=True,
                                               null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='MailActivity_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='MailActivity_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    calendar_event = models.ForeignKey(CalendarEvent, models.DO_NOTHING, related_name='MailActivity_calendar_event',
                                       blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_activity'


class MailActivityRel(models.Model):
    activity = models.ForeignKey('MailActivityType', models.DO_NOTHING, related_name='MailActivityRel_activity')
    recommended = models.ForeignKey('MailActivityType', models.DO_NOTHING, related_name='MailActivityRel_recommended')

    class Meta:
        managed = False
        db_table = 'mail_activity_rel'
        unique_together = (('activity', 'recommended'),)


class MailActivityType(models.Model):
    name = models.CharField(max_length=1000)
    summary = models.CharField(max_length=1000, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    delay_count = models.IntegerField(blank=True, null=True)
    delay_unit = models.CharField(max_length=1000)
    delay_from = models.CharField(max_length=1000)
    icon = models.CharField(max_length=1000, blank=True, null=True)
    decoration_type = models.CharField(max_length=1000, blank=True, null=True)
    res_model = models.ForeignKey(IrModel, models.DO_NOTHING, related_name='MailActivityType_res_model', blank=True,
                                  null=True)
    default_next_type = models.ForeignKey('self', models.DO_NOTHING, related_name='MailActivityType_default_next_type',
                                          blank=True, null=True)
    force_next = models.BooleanField(blank=True, null=True)
    category = models.CharField(max_length=1000, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='MailActivityType_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='MailActivityType_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_activity_type'


class MailActivityTypeMailTemplateRel(models.Model):
    mail_activity_type = models.ForeignKey(MailActivityType, models.DO_NOTHING)
    mail_template = models.ForeignKey('MailTemplate', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_activity_type_mail_template_rel'
        unique_together = (('mail_activity_type', 'mail_template'),)


class MailAlias(models.Model):
    alias_name = models.CharField(unique=True, max_length=1000, blank=True, null=True)
    alias_model = models.ForeignKey(IrModel, models.DO_NOTHING)
    alias_user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='MailAlias_alias_user', blank=True,
                                   null=True)
    alias_defaults = models.TextField()
    alias_force_thread_id = models.IntegerField(blank=True, null=True)
    alias_parent_model = models.ForeignKey(IrModel, models.DO_NOTHING, related_name='MailAlias_alias_parent_model',
                                           blank=True, null=True)
    alias_parent_thread_id = models.IntegerField(blank=True, null=True)
    alias_contact = models.CharField(max_length=1000)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='MailAlias_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='MailAlias_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_alias'


class MailBlacklist(models.Model):
    email = models.CharField(unique=True, max_length=1000)
    active = models.BooleanField(blank=True, null=True)
    message_main_attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING,
                                                related_name='MailBlacklist_message_main_attachment', blank=True,
                                                null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='MailBlacklist_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='MailBlacklist_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_blacklist'


class MailChannel(models.Model):
    name = models.CharField(max_length=1000)
    channel_type = models.CharField(max_length=1000, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    uuid = models.CharField(max_length=50, blank=True, null=True)
    email_send = models.BooleanField(blank=True, null=True)
    public = models.CharField(max_length=1000)
    group_public = models.ForeignKey('ResGroups', models.DO_NOTHING, related_name='MailChannel_group_public',
                                     blank=True, null=True)
    moderation = models.BooleanField(blank=True, null=True)
    moderation_notify = models.BooleanField(blank=True, null=True)
    moderation_notify_msg = models.TextField(blank=True, null=True)
    moderation_guidelines = models.BooleanField(blank=True, null=True)
    moderation_guidelines_msg = models.TextField(blank=True, null=True)
    alias = models.ForeignKey(MailAlias, models.DO_NOTHING)
    message_main_attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING,
                                                related_name='MailChannel_message_main_attachment', blank=True,
                                                null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='MailChannel_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='MailChannel_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_channel'


class MailChannelMailWizardInviteRel(models.Model):
    mail_wizard_invite = models.ForeignKey('MailWizardInvite', models.DO_NOTHING)
    mail_channel = models.ForeignKey(MailChannel, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_channel_mail_wizard_invite_rel'
        unique_together = (('mail_wizard_invite', 'mail_channel'),)


class MailChannelModeratorRel(models.Model):
    mail_channel = models.ForeignKey(MailChannel, models.DO_NOTHING)
    res_users = models.ForeignKey('ResUsers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_channel_moderator_rel'
        unique_together = (('mail_channel', 'res_users'),)


class MailChannelPartner(models.Model):
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name='MailChannelPartner_partner', blank=True,
                                null=True)
    channel = models.ForeignKey(MailChannel, models.DO_NOTHING, related_name='MailChannelPartner_channel', blank=True,
                                null=True)
    seen_message = models.ForeignKey('MailMessage', models.DO_NOTHING, related_name='MailChannelPartner_seen_message',
                                     blank=True, null=True)
    fold_state = models.CharField(max_length=1000, blank=True, null=True)
    is_minimized = models.BooleanField(blank=True, null=True)
    is_pinned = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='MailChannelPartner_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='MailChannelPartner_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_channel_partner'


class MailChannelResGroupsRel(models.Model):
    mail_channel = models.ForeignKey(MailChannel, models.DO_NOTHING)
    res_groups = models.ForeignKey('ResGroups', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_channel_res_groups_rel'
        unique_together = (('mail_channel', 'res_groups'),)


class MailComposeMessage(models.Model):
    composition_mode = models.CharField(max_length=1000, blank=True, null=True)
    use_active_domain = models.BooleanField(blank=True, null=True)
    active_domain = models.TextField(blank=True, null=True)
    is_log = models.BooleanField(blank=True, null=True)
    subject = models.CharField(max_length=1000, blank=True, null=True)
    notify = models.BooleanField(blank=True, null=True)
    auto_delete = models.BooleanField(blank=True, null=True)
    auto_delete_message = models.BooleanField(blank=True, null=True)
    template = models.ForeignKey('MailTemplate', models.DO_NOTHING, related_name='MailComposeMessage_template',
                                 blank=True, null=True)
    message_type = models.CharField(max_length=1000)
    subtype = models.ForeignKey('MailMessageSubtype', models.DO_NOTHING, related_name='MailComposeMessage_subtype',
                                blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    parent = models.ForeignKey('MailMessage', models.DO_NOTHING, related_name='MailComposeMessage_parent', blank=True,
                               null=True)
    model = models.CharField(max_length=1000, blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)
    record_name = models.CharField(max_length=1000, blank=True, null=True)
    mail_activity_type = models.ForeignKey(MailActivityType, models.DO_NOTHING,
                                           related_name='MailComposeMessage_mail_activity_type', blank=True, null=True)
    email_from = models.CharField(max_length=1000, blank=True, null=True)
    author = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name='MailComposeMessage_author', blank=True,
                               null=True)
    no_auto_thread = models.BooleanField(blank=True, null=True)
    message_id = models.CharField(max_length=1000, blank=True, null=True)
    reply_to = models.CharField(max_length=1000, blank=True, null=True)
    mail_server = models.ForeignKey(IrMailServer, models.DO_NOTHING, related_name='MailComposeMessage_mail_server',
                                    blank=True, null=True)
    moderation_status = models.CharField(max_length=1000, blank=True, null=True)
    moderator = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='MailComposeMessage_moderator',
                                  blank=True, null=True)
    layout = models.CharField(max_length=1000, blank=True, null=True)
    add_sign = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='MailComposeMessage_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='MailComposeMessage_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_compose_message'


class MailComposeMessageIrAttachmentsRel(models.Model):
    wizard = models.ForeignKey(MailComposeMessage, models.DO_NOTHING)
    attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_compose_message_ir_attachments_rel'
        unique_together = (('wizard', 'attachment'),)


class MailComposeMessageResPartnerRel(models.Model):
    wizard = models.ForeignKey(MailComposeMessage, models.DO_NOTHING)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_compose_message_res_partner_rel'
        unique_together = (('wizard', 'partner'),)


class MailFollowers(models.Model):
    res_model = models.CharField(max_length=1000)
    res_id = models.IntegerField(blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name='MailFollowers_partner', blank=True,
                                null=True)
    channel = models.ForeignKey(MailChannel, models.DO_NOTHING, related_name='MailFollowers_channel', blank=True,
                                null=True)

    class Meta:
        managed = False
        db_table = 'mail_followers'
        unique_together = (('res_model', 'res_id', 'channel'), ('res_model', 'res_id', 'partner'),)


class MailFollowersMailMessageSubtypeRel(models.Model):
    mail_followers = models.ForeignKey(MailFollowers, models.DO_NOTHING)
    mail_message_subtype = models.ForeignKey('MailMessageSubtype', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_followers_mail_message_subtype_rel'
        unique_together = (('mail_followers', 'mail_message_subtype'),)


class MailMail(models.Model):
    mail_message = models.ForeignKey('MailMessage', models.DO_NOTHING)
    body_html = models.TextField(blank=True, null=True)
    references = models.TextField(blank=True, null=True)
    headers = models.TextField(blank=True, null=True)
    notification = models.BooleanField(blank=True, null=True)
    email_to = models.TextField(blank=True, null=True)
    email_cc = models.CharField(max_length=1000, blank=True, null=True)
    state = models.CharField(max_length=1000, blank=True, null=True)
    auto_delete = models.BooleanField(blank=True, null=True)
    failure_reason = models.TextField(blank=True, null=True)
    scheduled_date = models.CharField(max_length=1000, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='MailMail_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='MailMail_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    fetchmail_server = models.ForeignKey(FetchmailServer, models.DO_NOTHING, related_name='MailMail_fetchmail_server',
                                         blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_mail'


class MailMailResPartnerRel(models.Model):
    mail_mail = models.ForeignKey(MailMail, models.DO_NOTHING)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_mail_res_partner_rel'
        unique_together = (('mail_mail', 'res_partner'),)


class MailMessage(models.Model):
    subject = models.CharField(max_length=1000, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, related_name='MailMessage_parent', blank=True, null=True)
    model = models.CharField(max_length=1000, blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)
    record_name = models.CharField(max_length=1000, blank=True, null=True)
    message_type = models.CharField(max_length=1000)
    subtype = models.ForeignKey('MailMessageSubtype', models.DO_NOTHING, related_name='MailMessage_subtype', blank=True,
                                null=True)
    mail_activity_type = models.ForeignKey(MailActivityType, models.DO_NOTHING,
                                           related_name='MailMessage_mail_activity_type', blank=True, null=True)
    email_from = models.CharField(max_length=1000, blank=True, null=True)
    author = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name='MailMessage_author', blank=True,
                               null=True)
    no_auto_thread = models.BooleanField(blank=True, null=True)
    message_id = models.CharField(max_length=1000, blank=True, null=True)
    reply_to = models.CharField(max_length=1000, blank=True, null=True)
    mail_server = models.ForeignKey(IrMailServer, models.DO_NOTHING, related_name='MailMessage_mail_server', blank=True,
                                    null=True)
    moderation_status = models.CharField(max_length=1000, blank=True, null=True)
    moderator = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='MailMessage_moderator', blank=True,
                                  null=True)
    layout = models.CharField(max_length=1000, blank=True, null=True)
    add_sign = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='MailMessage_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='MailMessage_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_message'


class MailMessageMailChannelRel(models.Model):
    mail_message = models.ForeignKey(MailMessage, models.DO_NOTHING)
    mail_channel = models.ForeignKey(MailChannel, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_message_mail_channel_rel'
        unique_together = (('mail_message', 'mail_channel'),)


class MailMessageResPartnerNeedactionRel(models.Model):
    mail_message = models.ForeignKey(MailMessage, models.DO_NOTHING)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)
    is_read = models.BooleanField(blank=True, null=True)
    is_email = models.BooleanField(blank=True, null=True)
    email_status = models.CharField(max_length=1000, blank=True, null=True)
    mail = models.ForeignKey(MailMail, models.DO_NOTHING, related_name='MailMessageResPartnerNeedactionRel_mail',
                             blank=True, null=True)
    failure_type = models.CharField(max_length=1000, blank=True, null=True)
    failure_reason = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_message_res_partner_needaction_rel'


class MailMessageResPartnerNeedactionRelMailResendMessageRel(models.Model):
    mail_resend_message = models.ForeignKey('MailResendMessage', models.DO_NOTHING)
    mail_message_res_partner_needaction_rel = models.ForeignKey(MailMessageResPartnerNeedactionRel, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_message_res_partner_needaction_rel_mail_resend_message_rel'
        unique_together = (('mail_resend_message', 'mail_message_res_partner_needaction_rel'),)


class MailMessageResPartnerRel(models.Model):
    mail_message = models.ForeignKey(MailMessage, models.DO_NOTHING)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_message_res_partner_rel'
        unique_together = (('mail_message', 'res_partner'),)


class MailMessageResPartnerStarredRel(models.Model):
    mail_message = models.ForeignKey(MailMessage, models.DO_NOTHING)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_message_res_partner_starred_rel'
        unique_together = (('mail_message', 'res_partner'),)


class MailMessageSubtype(models.Model):
    name = models.CharField(max_length=1000)
    description = models.TextField(blank=True, null=True)
    internal = models.BooleanField(blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, related_name='MailMessageSubtype_parent', blank=True,
                               null=True)
    relation_field = models.CharField(max_length=1000, blank=True, null=True)
    res_model = models.CharField(max_length=1000, blank=True, null=True)
    default = models.BooleanField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    hidden = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='MailMessageSubtype_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='MailMessageSubtype_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_message_subtype'


class MailModeration(models.Model):
    email = models.CharField(max_length=1000)
    status = models.CharField(max_length=1000)
    channel = models.ForeignKey(MailChannel, models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='MailModeration_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='MailModeration_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_moderation'
        unique_together = (('email', 'channel'),)


class MailResendCancel(models.Model):
    model = models.CharField(max_length=1000, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='MailResendCancel_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='MailResendCancel_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_resend_cancel'


class MailResendMessage(models.Model):
    mail_message = models.ForeignKey(MailMessage, models.DO_NOTHING, related_name='MailResendMessage_mail_message',
                                     blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='MailResendMessage_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='MailResendMessage_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_resend_message'


class MailResendPartner(models.Model):
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)
    resend = models.BooleanField(blank=True, null=True)
    resend_wizard = models.ForeignKey(MailResendMessage, models.DO_NOTHING,
                                      related_name='MailResendPartner_resend_wizard', blank=True, null=True)
    message = models.CharField(max_length=1000, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='MailResendPartner_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='MailResendPartner_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_resend_partner'


class MailShortcode(models.Model):
    source = models.CharField(max_length=1000)
    substitution = models.TextField()
    description = models.CharField(max_length=1000, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='MailShortcode_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='MailShortcode_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_shortcode'


class MailTemplate(models.Model):
    name = models.CharField(max_length=1000, blank=True, null=True)
    model_id = models.ForeignKey(IrModel, models.DO_NOTHING, related_name='MailTemplate_ir_model', blank=True,
                                 null=True)
    model = models.CharField(db_column='model', max_length=1000, blank=True,
                             null=True)  # Field renamed because of name conflict.
    lang = models.CharField(max_length=1000, blank=True, null=True)
    user_signature = models.BooleanField(blank=True, null=True)
    subject = models.CharField(max_length=1000, blank=True, null=True)
    email_from = models.CharField(max_length=1000, blank=True, null=True)
    use_default_to = models.BooleanField(blank=True, null=True)
    email_to = models.CharField(max_length=1000, blank=True, null=True)
    partner_to = models.CharField(max_length=1000, blank=True, null=True)
    email_cc = models.CharField(max_length=1000, blank=True, null=True)
    reply_to = models.CharField(max_length=1000, blank=True, null=True)
    mail_server = models.ForeignKey(IrMailServer, models.DO_NOTHING, related_name='MailTemplate_main_server',
                                    blank=True, null=True)
    body_html = models.TextField(blank=True, null=True)
    report_name = models.CharField(max_length=1000, blank=True, null=True)
    report_template = models.ForeignKey(IrActReportXml, models.DO_NOTHING, related_name='MailTemplate_report_template',
                                        db_column='report_template', blank=True, null=True)
    ref_ir_act_window = models.ForeignKey(IrActWindow, models.DO_NOTHING, related_name='MailTemplate_ref_ir_act_window',
                                          db_column='ref_ir_act_window', blank=True, null=True)
    auto_delete = models.BooleanField(blank=True, null=True)
    model_object_field = models.ForeignKey(IrModelFields, models.DO_NOTHING,
                                           related_name='MailTemplate_model_object_field',
                                           db_column='model_object_field', blank=True, null=True)
    sub_object = models.ForeignKey(IrModel, models.DO_NOTHING, related_name='MailTemplate_sub_object',
                                   db_column='sub_object', blank=True, null=True)
    sub_model_object_field = models.ForeignKey(IrModelFields, models.DO_NOTHING,
                                               related_name='MailTemplate_sub_model_object_field',
                                               db_column='sub_model_object_field', blank=True, null=True)
    null_value = models.CharField(max_length=1000, blank=True, null=True)
    copyvalue = models.CharField(max_length=1000, blank=True, null=True)
    scheduled_date = models.CharField(max_length=1000, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='MailTemplate_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='MailTemplate_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_template'


class MailTrackingValue(models.Model):
    field = models.CharField(max_length=1000)
    field_desc = models.CharField(max_length=1000)
    field_type = models.CharField(max_length=1000, blank=True, null=True)
    old_value_integer = models.IntegerField(blank=True, null=True)
    old_value_float = models.FloatField(blank=True, null=True)
    old_value_monetary = models.FloatField(blank=True, null=True)
    old_value_char = models.CharField(max_length=1000, blank=True, null=True)
    old_value_text = models.TextField(blank=True, null=True)
    old_value_datetime = models.DateTimeField(blank=True, null=True)
    new_value_integer = models.IntegerField(blank=True, null=True)
    new_value_float = models.FloatField(blank=True, null=True)
    new_value_monetary = models.FloatField(blank=True, null=True)
    new_value_char = models.CharField(max_length=1000, blank=True, null=True)
    new_value_text = models.TextField(blank=True, null=True)
    new_value_datetime = models.DateTimeField(blank=True, null=True)
    mail_message = models.ForeignKey(MailMessage, models.DO_NOTHING)
    track_sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='MailTrackingValue_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='MailTrackingValue_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_tracking_value'


class MailWizardInvite(models.Model):
    res_model = models.CharField(max_length=1000)
    res_id = models.IntegerField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    send_mail = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='MailWizardInvite_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='MailWizardInvite_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_wizard_invite'


class MailWizardInviteResPartnerRel(models.Model):
    mail_wizard_invite = models.ForeignKey(MailWizardInvite, models.DO_NOTHING)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_wizard_invite_res_partner_rel'
        unique_together = (('mail_wizard_invite', 'res_partner'),)


class MeetingCategoryRel(models.Model):
    event = models.ForeignKey(CalendarEvent, models.DO_NOTHING)
    type = models.ForeignKey(CalendarEventType, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'meeting_category_rel'
        unique_together = (('event', 'type'),)


class MergeOpportunityRel(models.Model):
    merge = models.ForeignKey(CrmMergeOpportunity, models.DO_NOTHING)
    opportunity = models.ForeignKey(CrmLead, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'merge_opportunity_rel'
        unique_together = (('merge', 'opportunity'),)


class MessageAttachmentRel(models.Model):
    message = models.ForeignKey(MailMessage, models.DO_NOTHING)
    attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'message_attachment_rel'
        unique_together = (('message', 'attachment'),)


class PortalShare(models.Model):
    res_model = models.CharField(max_length=1000)
    res_id = models.IntegerField()
    note = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='PortalShare_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='PortalShare_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'portal_share'


class PortalShareResPartnerRel(models.Model):
    portal_share = models.ForeignKey(PortalShare, models.DO_NOTHING)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'portal_share_res_partner_rel'
        unique_together = (('portal_share', 'res_partner'),)


class PortalWizard(models.Model):
    welcome_message = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='PortalWizard_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='PortalWizard_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'portal_wizard'


class PortalWizardUser(models.Model):
    wizard = models.ForeignKey(PortalWizard, models.DO_NOTHING)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)
    email = models.CharField(max_length=1000, blank=True, null=True)
    in_portal = models.BooleanField(blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='PortalWizardUser_user', blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='PortalWizardUser_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='PortalWizardUser_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'portal_wizard_user'


class ProjectFavoriteUserRel(models.Model):
    project = models.ForeignKey('ProjectProject', models.DO_NOTHING)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'project_favorite_user_rel'
        unique_together = (('project', 'user'),)


class ProjectProject(models.Model):
    access_token = models.CharField(max_length=1000, blank=True, null=True)
    message_main_attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING,
                                                related_name='ProjectProject_message_main_attachment', blank=True,
                                                null=True)
    name = models.CharField(max_length=1000)
    active = models.BooleanField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name='ProjectProject_partner', blank=True,
                                null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    label_tasks = models.CharField(max_length=1000, blank=True, null=True)
    resource_calendar = models.ForeignKey('ResourceCalendar', models.DO_NOTHING,
                                          related_name='ProjectProject_resource_calendar', blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ProjectProject_user', blank=True, null=True)
    alias = models.ForeignKey(MailAlias, models.DO_NOTHING)
    privacy_visibility = models.CharField(max_length=1000)
    date_start = models.DateField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    subtask_project = models.ForeignKey('self', models.DO_NOTHING, related_name='ProjectProject_subtask_project',
                                        blank=True, null=True)
    percentage_satisfaction_task = models.IntegerField(blank=True, null=True)
    percentage_satisfaction_project = models.IntegerField(blank=True, null=True)
    rating_request_deadline = models.DateTimeField(blank=True, null=True)
    rating_status = models.CharField(max_length=1000)
    rating_status_period = models.CharField(max_length=1000, blank=True, null=True)
    portal_show_rating = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ProjectProject_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ProjectProject_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_project'


class ProjectTags(models.Model):
    name = models.CharField(unique=True, max_length=1000)
    color = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ProjectTags_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ProjectTags_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_tags'


class ProjectTagsProjectTaskRel(models.Model):
    project_task = models.ForeignKey('ProjectTask', models.DO_NOTHING)
    project_tags = models.ForeignKey(ProjectTags, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'project_tags_project_task_rel'
        unique_together = (('project_task', 'project_tags'),)


class ProjectTask(models.Model):
    access_token = models.CharField(max_length=1000, blank=True, null=True)
    rating_last_value = models.FloatField(blank=True, null=True)
    message_main_attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING,
                                                related_name='ProjectTask_message_main_attachment', blank=True,
                                                null=True)
    active = models.BooleanField(blank=True, null=True)
    name = models.CharField(max_length=1000)
    description = models.TextField(blank=True, null=True)
    priority = models.CharField(max_length=1000, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    stage = models.ForeignKey('ProjectTaskType', models.DO_NOTHING, related_name='ProjectTask_stage', blank=True,
                              null=True)
    kanban_state = models.CharField(max_length=1000)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date_start = models.DateTimeField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)
    date_assign = models.DateTimeField(blank=True, null=True)
    date_deadline = models.DateField(blank=True, null=True)
    date_last_stage_update = models.DateTimeField(blank=True, null=True)
    project = models.ForeignKey(ProjectProject, models.DO_NOTHING, related_name='ProjectTask_project', blank=True,
                                null=True)
    notes = models.TextField(blank=True, null=True)
    planned_hours = models.FloatField(blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ProjectTask_user', blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name='ProjectTask_partner', blank=True,
                                null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, related_name='ProjectTask_company', blank=True,
                                null=True)
    color = models.IntegerField(blank=True, null=True)
    displayed_image = models.ForeignKey(IrAttachment, models.DO_NOTHING, related_name='ProjectTask_displayed_image',
                                        blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, related_name='ProjectTask_parent', blank=True, null=True)
    email_from = models.CharField(max_length=1000, blank=True, null=True)
    email_cc = models.CharField(max_length=1000, blank=True, null=True)
    working_hours_open = models.FloatField(blank=True, null=True)
    working_hours_close = models.FloatField(blank=True, null=True)
    working_days_open = models.FloatField(blank=True, null=True)
    working_days_close = models.FloatField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ProjectTask_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ProjectTask_write_uid',
                                  db_column='write_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_task'


class ProjectTaskType(models.Model):
    name = models.CharField(max_length=1000)
    description = models.TextField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    legend_priority = models.CharField(max_length=1000, blank=True, null=True)
    legend_blocked = models.CharField(max_length=1000)
    legend_done = models.CharField(max_length=1000)
    legend_normal = models.CharField(max_length=1000)
    mail_template = models.ForeignKey(MailTemplate, models.DO_NOTHING, related_name='ProjectTaskType_mail_template',
                                      blank=True, null=True)
    fold = models.BooleanField(blank=True, null=True)
    rating_template = models.ForeignKey(MailTemplate, models.DO_NOTHING, related_name='ProjectTaskType_rating_template',
                                        blank=True, null=True)
    auto_validation_kanban_state = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ProjectTaskType_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ProjectTaskType_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_task_type'


class ProjectTaskTypeRel(models.Model):
    type = models.ForeignKey(ProjectTaskType, models.DO_NOTHING)
    project = models.ForeignKey(ProjectProject, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'project_task_type_rel'
        unique_together = (('type', 'project'),)


class RatingRating(models.Model):
    res_name = models.CharField(max_length=1000, blank=True, null=True)
    res_model = models.ForeignKey(IrModel, models.DO_NOTHING, related_name='RatingRating_res_model', blank=True,
                                  null=True)
    res_model_0 = models.CharField(db_column='res_model', max_length=1000, blank=True,
                                   null=True)  # Field renamed because of name conflict.
    res_id = models.IntegerField()
    parent_res_name = models.CharField(max_length=1000, blank=True, null=True)
    parent_res_model = models.ForeignKey(IrModel, models.DO_NOTHING, related_name='RatingRating_parent_res_model',
                                         blank=True, null=True)
    parent_res_model_0 = models.CharField(db_column='parent_res_model', max_length=1000, blank=True,
                                          null=True)  # Field renamed because of name conflict.
    parent_res_id = models.IntegerField(blank=True, null=True)
    rated_partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name='RatingRating_rated_partner',
                                      blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, related_name='RatingRating_partner', blank=True,
                                null=True)
    rating = models.FloatField(blank=True, null=True)
    rating_text = models.CharField(max_length=1000, blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)
    message = models.ForeignKey(MailMessage, models.DO_NOTHING, related_name='RatingRating_message', blank=True,
                                null=True)
    access_token = models.CharField(max_length=1000, blank=True, null=True)
    consumed = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='RatingRating_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='RatingRating_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rating_rating'


class RelModulesLangexport(models.Model):
    wiz = models.ForeignKey(BaseLanguageExport, models.DO_NOTHING)
    module = models.ForeignKey(IrModuleModule, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'rel_modules_langexport'
        unique_together = (('wiz', 'module'),)


class RelServerActions(models.Model):
    server = models.ForeignKey(IrActServer, models.DO_NOTHING, related_name='RelServerActions_server')
    action = models.ForeignKey(IrActServer, models.DO_NOTHING, related_name='RelServerActions_action')

    class Meta:
        managed = False
        db_table = 'rel_server_actions'
        unique_together = (('server', 'action'),)


class ReportLayout(models.Model):
    view = models.ForeignKey(IrUiView, models.DO_NOTHING)
    image = models.CharField(max_length=1000, blank=True, null=True)
    pdf = models.CharField(max_length=1000, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ReportLayout_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ReportLayout_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_layout'


class ReportPaperformat(models.Model):
    name = models.CharField(max_length=1000)
    default = models.BooleanField(blank=True, null=True)
    format = models.CharField(max_length=1000, blank=True, null=True)
    margin_top = models.FloatField(blank=True, null=True)
    margin_bottom = models.FloatField(blank=True, null=True)
    margin_left = models.FloatField(blank=True, null=True)
    margin_right = models.FloatField(blank=True, null=True)
    page_height = models.IntegerField(blank=True, null=True)
    page_width = models.IntegerField(blank=True, null=True)
    orientation = models.CharField(max_length=1000, blank=True, null=True)
    header_line = models.BooleanField(blank=True, null=True)
    header_spacing = models.IntegerField(blank=True, null=True)
    dpi = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ReportPaperformat_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ReportPaperformat_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_paperformat'


class ResBank(models.Model):
    name = models.CharField(max_length=1000)
    street = models.CharField(max_length=1000, blank=True, null=True)
    street2 = models.CharField(max_length=1000, blank=True, null=True)
    zip = models.CharField(max_length=1000, blank=True, null=True)
    city = models.CharField(max_length=1000, blank=True, null=True)
    state = models.ForeignKey('ResCountryState', models.DO_NOTHING, related_name='ResBank_state', db_column='state',
                              blank=True, null=True)
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, related_name='ResBank_country', db_column='country',
                                blank=True, null=True)
    email = models.CharField(max_length=1000, blank=True, null=True)
    phone = models.CharField(max_length=1000, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    bic = models.CharField(max_length=1000, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ResBank_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ResBank_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_bank'


class ResCompany(models.Model):
    name = models.CharField(unique=True, max_length=1000)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING)
    sequence = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, related_name='ResCompany_parent', blank=True, null=True)
    report_header = models.TextField(blank=True, null=True)
    report_footer = models.TextField(blank=True, null=True)
    logo_web = models.BinaryField(blank=True, null=True)
    account_no = models.CharField(max_length=1000, blank=True, null=True)
    email = models.CharField(max_length=1000, blank=True, null=True)
    phone = models.CharField(max_length=1000, blank=True, null=True)
    company_registry = models.CharField(max_length=1000, blank=True, null=True)
    paperformat = models.ForeignKey(ReportPaperformat, models.DO_NOTHING, related_name='ResCompany_paperformat',
                                    blank=True, null=True)
    external_report_layout = models.ForeignKey(IrUiView, models.DO_NOTHING,
                                               related_name='ResCompany_external_report_layout', blank=True, null=True)
    base_onboarding_company_state = models.CharField(max_length=1000, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ResCompany_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ResCompany_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    resource_calendar = models.ForeignKey('ResourceCalendar', models.DO_NOTHING,
                                          related_name='ResCompany_resource_calendar', blank=True, null=True)
    partner_gid = models.IntegerField(blank=True, null=True)
    snailmail_color = models.BooleanField(blank=True, null=True)
    snailmail_duplex = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_company'


class ResCompanyUsersRel(models.Model):
    cid = models.ForeignKey(ResCompany, models.DO_NOTHING, related_name='ResCompanyUsersRel_cid', db_column='cid')
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'res_company_users_rel'
        unique_together = (('cid', 'user'),)


class ResConfig(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ResConfig_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ResConfig_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_config'


class ResConfigInstaller(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ResConfigInstaller_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ResConfigInstaller_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_config_installer'


class ResConfigSettings(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ResConfigSettings_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ResConfigSettings_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    group_multi_company = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    user_default_rights = models.BooleanField(blank=True, null=True)
    external_email_server_default = models.BooleanField(blank=True, null=True)
    module_base_import = models.BooleanField(blank=True, null=True)
    module_google_calendar = models.BooleanField(blank=True, null=True)
    module_google_drive = models.BooleanField(blank=True, null=True)
    module_google_spreadsheet = models.BooleanField(blank=True, null=True)
    module_auth_oauth = models.BooleanField(blank=True, null=True)
    module_auth_ldap = models.BooleanField(blank=True, null=True)
    module_base_gengo = models.BooleanField(blank=True, null=True)
    module_inter_company_rules = models.BooleanField(blank=True, null=True)
    module_pad = models.BooleanField(blank=True, null=True)
    module_voip = models.BooleanField(blank=True, null=True)
    module_web_unsplash = models.BooleanField(blank=True, null=True)
    module_partner_autocomplete = models.BooleanField(blank=True, null=True)
    company_share_partner = models.BooleanField(blank=True, null=True)
    group_multi_currency = models.BooleanField(blank=True, null=True)
    show_effect = models.BooleanField(blank=True, null=True)
    fail_counter = models.IntegerField(blank=True, null=True)
    alias_domain = models.CharField(max_length=1000, blank=True, null=True)
    unsplash_access_key = models.CharField(max_length=1000, blank=True, null=True)
    auth_signup_reset_password = models.BooleanField(blank=True, null=True)
    auth_signup_uninvited = models.CharField(max_length=1000, blank=True, null=True)
    auth_signup_template_user = models.ForeignKey('ResUsers', models.DO_NOTHING,
                                                  related_name='ResConfigSettings_auth_signup_template_user',
                                                  blank=True, null=True)
    digest_emails = models.BooleanField(blank=True, null=True)
    digest = models.ForeignKey(DigestDigest, models.DO_NOTHING, related_name='ResConfigSettings_digest', blank=True,
                               null=True)
    module_project_forecast = models.BooleanField(blank=True, null=True)
    module_hr_timesheet = models.BooleanField(blank=True, null=True)
    group_subtask_project = models.BooleanField(blank=True, null=True)
    group_project_rating = models.BooleanField(blank=True, null=True)
    crm_alias_prefix = models.CharField(max_length=1000, blank=True, null=True)
    generate_lead_from_alias = models.BooleanField(blank=True, null=True)
    group_use_lead = models.BooleanField(blank=True, null=True)
    module_crm_phone_validation = models.BooleanField(blank=True, null=True)
    module_crm_reveal = models.BooleanField(blank=True, null=True)
    module_hr_org_chart = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_config_settings'


class ResCountry(models.Model):
    name = models.CharField(unique=True, max_length=1000)
    code = models.CharField(unique=True, max_length=2, blank=True, null=True)
    address_format = models.TextField(blank=True, null=True)
    address_view = models.ForeignKey(IrUiView, models.DO_NOTHING, related_name='ResCountry_address_view', blank=True,
                                     null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, related_name='ResCountry_currency', blank=True,
                                 null=True)
    phone_code = models.IntegerField(blank=True, null=True)
    name_position = models.CharField(max_length=1000, blank=True, null=True)
    vat_label = models.CharField(max_length=1000, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ResCountry_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ResCountry_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_country'


class ResCountryGroup(models.Model):
    name = models.CharField(max_length=1000)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ResCountryGroup_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ResCountryGroup_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_country_group'


class ResCountryResCountryGroupRel(models.Model):
    res_country = models.ForeignKey(ResCountry, models.DO_NOTHING)
    res_country_group = models.ForeignKey(ResCountryGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'res_country_res_country_group_rel'
        unique_together = (('res_country', 'res_country_group'),)


class ResCountryState(models.Model):
    country = models.ForeignKey(ResCountry, models.DO_NOTHING)
    name = models.CharField(max_length=1000)
    code = models.CharField(max_length=1000)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ResCountryState_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ResCountryState_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_country_state'
        unique_together = (('country', 'code'),)


class ResCurrency(models.Model):
    name = models.CharField(unique=True, max_length=1000)
    symbol = models.CharField(max_length=1000)
    rounding = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    decimal_places = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    position = models.CharField(max_length=1000, blank=True, null=True)
    currency_unit_label = models.CharField(max_length=1000, blank=True, null=True)
    currency_subunit_label = models.CharField(max_length=1000, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ResCurrency_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ResCurrency_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_currency'


class ResCurrencyRate(models.Model):
    name = models.DateField()
    rate = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    currency = models.ForeignKey(ResCurrency, models.DO_NOTHING, related_name='ResCurrencyRate_currency', blank=True,
                                 null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, related_name='ResCurrencyRate_company', blank=True,
                                null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ResCurrencyRate_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ResCurrencyRate_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_currency_rate'
        unique_together = (('name', 'currency', 'company'),)


class ResGroups(models.Model):
    name = models.CharField(max_length=1000)
    comment = models.TextField(blank=True, null=True)
    category = models.ForeignKey(IrModuleCategory, models.DO_NOTHING, related_name='ResGroups_category', blank=True,
                                 null=True)
    color = models.IntegerField(blank=True, null=True)
    share = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ResGroups_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ResGroups_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_groups'
        unique_together = (('category', 'name'),)


class ResGroupsImpliedRel(models.Model):
    gid = models.ForeignKey(ResGroups, models.DO_NOTHING, related_name='ResGroupsImpliedRel_gid', db_column='gid')
    hid = models.ForeignKey(ResGroups, models.DO_NOTHING, related_name='ResGroupsImpliedRel_hid', db_column='hid')

    class Meta:
        managed = False
        db_table = 'res_groups_implied_rel'
        unique_together = (('gid', 'hid'),)


class ResGroupsReportRel(models.Model):
    uid = models.ForeignKey(IrActReportXml, models.DO_NOTHING, related_name='ResGroupsReportRel_uid', db_column='uid')
    gid = models.ForeignKey(ResGroups, models.DO_NOTHING, related_name='ResGroupsReportRel_gid', db_column='gid')

    class Meta:
        managed = False
        db_table = 'res_groups_report_rel'
        unique_together = (('uid', 'gid'),)


class ResGroupsUsersRel(models.Model):
    gid = models.ForeignKey(ResGroups, models.DO_NOTHING, related_name='ResGroupsUsersRel_gid', db_column='gid')
    uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ResGroupsUsersRel_uid', db_column='uid')

    class Meta:
        managed = False
        db_table = 'res_groups_users_rel'
        unique_together = (('gid', 'uid'),)


class ResLang(models.Model):
    name = models.CharField(unique=True, max_length=1000)
    code = models.CharField(unique=True, max_length=1000)
    iso_code = models.CharField(max_length=1000, blank=True, null=True)
    translatable = models.BooleanField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    direction = models.CharField(max_length=1000)
    date_format = models.CharField(max_length=1000)
    time_format = models.CharField(max_length=1000)
    week_start = models.IntegerField()
    grouping = models.CharField(max_length=1000)
    decimal_point = models.CharField(max_length=1000)
    thousands_sep = models.CharField(max_length=1000, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ResLang_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ResLang_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_lang'


class ResPartner(models.Model):
    name = models.CharField(max_length=1000, blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, related_name='ResPartner_company', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    display_name = models.CharField(max_length=1000, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    title = models.ForeignKey('ResPartnerTitle', models.DO_NOTHING, related_name='ResPartner_title', db_column='title',
                              blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, related_name='ResPartner_parent', blank=True, null=True)
    ref = models.CharField(max_length=1000, blank=True, null=True)
    lang = models.CharField(max_length=1000, blank=True, null=True)
    tz = models.CharField(max_length=1000, blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ResPartner_user', blank=True, null=True)
    vat = models.CharField(max_length=1000, blank=True, null=True)
    website = models.CharField(max_length=1000, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    credit_limit = models.FloatField(blank=True, null=True)
    barcode = models.CharField(max_length=1000, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    customer = models.BooleanField(blank=True, null=True)
    supplier = models.BooleanField(blank=True, null=True)
    employee = models.BooleanField(blank=True, null=True)
    function = models.CharField(max_length=1000, blank=True, null=True)
    type = models.CharField(max_length=1000, blank=True, null=True)
    street = models.CharField(max_length=1000, blank=True, null=True)
    street2 = models.CharField(max_length=1000, blank=True, null=True)
    zip = models.CharField(max_length=1000, blank=True, null=True)
    city = models.CharField(max_length=1000, blank=True, null=True)
    state = models.ForeignKey(ResCountryState, models.DO_NOTHING, related_name='ResPartner_state', blank=True,
                              null=True)
    country = models.ForeignKey(ResCountry, models.DO_NOTHING, related_name='ResPartner_country', blank=True, null=True)
    email = models.CharField(max_length=1000, blank=True, null=True)
    phone = models.CharField(max_length=1000, blank=True, null=True)
    mobile = models.CharField(max_length=1000, blank=True, null=True)
    is_company = models.BooleanField(blank=True, null=True)
    industry = models.ForeignKey('ResPartnerIndustry', models.DO_NOTHING, related_name='ResPartner_industry',
                                 blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    partner_share = models.BooleanField(blank=True, null=True)
    commercial_partner = models.ForeignKey('self', models.DO_NOTHING, related_name='ResPartner_commercial_partner',
                                           blank=True, null=True)
    commercial_company_name = models.CharField(max_length=1000, blank=True, null=True)
    company_name = models.CharField(max_length=1000, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ResPartner_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ResPartner_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    message_main_attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING,
                                                related_name='ResPartner_message_main_attachment', blank=True,
                                                null=True)
    message_bounce = models.IntegerField(blank=True, null=True)
    signup_token = models.CharField(max_length=1000, blank=True, null=True)
    signup_type = models.CharField(max_length=1000, blank=True, null=True)
    signup_expiration = models.DateTimeField(blank=True, null=True)
    partner_gid = models.IntegerField(blank=True, null=True)
    additional_info = models.CharField(max_length=1000, blank=True, null=True)
    calendar_last_notif_ack = models.DateTimeField(blank=True, null=True)
    team = models.ForeignKey(CrmTeam, models.DO_NOTHING, related_name='ResPartner_team', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_partner'


class ResPartnerAutocompleteSync(models.Model):
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING, related_name='ResPartnerAutocompleteSync_partner',
                                blank=True, null=True)
    synched = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ResPartnerAutocompleteSync_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ResPartnerAutocompleteSync_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_partner_autocomplete_sync'


class ResPartnerBank(models.Model):
    acc_number = models.CharField(max_length=1000)
    sanitized_acc_number = models.CharField(max_length=1000, blank=True, null=True)
    acc_holder_name = models.CharField(max_length=1000, blank=True, null=True)
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING)
    bank = models.ForeignKey(ResBank, models.DO_NOTHING, related_name='ResPartnerBank_bank', blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    currency = models.ForeignKey(ResCurrency, models.DO_NOTHING, related_name='ResPartnerBank_currency', blank=True,
                                 null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, related_name='ResPartnerBank_company', blank=True,
                                null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ResPartnerBank_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ResPartnerBank_wtire_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_partner_bank'
        unique_together = (('sanitized_acc_number', 'company'),)


class ResPartnerCategory(models.Model):
    parent_path = models.CharField(max_length=1000, blank=True, null=True)
    name = models.CharField(max_length=1000)
    color = models.IntegerField(blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, related_name='ResPartnerCategory_parent', blank=True,
                               null=True)
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ResPartnerCategory_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ResPartnerCategory_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_partner_category'


class ResPartnerIndustry(models.Model):
    name = models.CharField(max_length=1000, blank=True, null=True)
    full_name = models.CharField(max_length=1000, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ResPartnerIndustry_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ResPartnerIndustry_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_partner_industry'


class ResPartnerResPartnerCategoryRel(models.Model):
    category = models.ForeignKey(ResPartnerCategory, models.DO_NOTHING)
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'res_partner_res_partner_category_rel'
        unique_together = (('category', 'partner'),)


class ResPartnerTitle(models.Model):
    name = models.CharField(max_length=1000)
    shortcut = models.CharField(max_length=1000, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ResPartnerTitle_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, related_name='ResPartnerTitle_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_partner_title'


class ResUsers(models.Model):
    active = models.BooleanField(blank=True, null=True)
    login = models.CharField(unique=True, max_length=1000)
    password = models.CharField(max_length=1000, blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING)
    create_date = models.DateTimeField(blank=True, null=True)
    signature = models.TextField(blank=True, null=True)
    action_id = models.IntegerField(blank=True, null=True)
    share = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey('self', models.DO_NOTHING, related_name='ResUsers_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('self', models.DO_NOTHING, related_name='ResUsers_write_uid', db_column='write_uid',
                                  blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    alias = models.ForeignKey(MailAlias, models.DO_NOTHING, related_name='ResUsers_alias', blank=True, null=True)
    notification_type = models.CharField(max_length=1000)
    odoobot_state = models.CharField(max_length=1000)
    sale_team = models.ForeignKey(CrmTeam, models.DO_NOTHING, related_name='ResUsers_sale_team', blank=True, null=True)
    target_sales_won = models.IntegerField(blank=True, null=True)
    target_sales_done = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_users'


class ResUsersLog(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, related_name='ResUsersLog_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, related_name='ResUsersLog_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_users_log'


class ResourceCalendar(models.Model):
    name = models.CharField(max_length=1000)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, related_name='ResourceCalendar_company', blank=True,
                                null=True)
    hours_per_day = models.FloatField(blank=True, null=True)
    tz = models.CharField(max_length=1000)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, related_name='ResourceCalendar_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, related_name='ResourceCalendar_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resource_calendar'


class ResourceCalendarAttendance(models.Model):
    name = models.CharField(max_length=1000)
    dayofweek = models.CharField(max_length=1000)
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    hour_from = models.FloatField()
    hour_to = models.FloatField()
    calendar = models.ForeignKey(ResourceCalendar, models.DO_NOTHING)
    day_period = models.CharField(max_length=1000)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, related_name='ResourceCalendarAttendance_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, related_name='ResourceCalendarAttendance_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resource_calendar_attendance'


class ResourceCalendarLeaves(models.Model):
    name = models.CharField(max_length=1000, blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, related_name='ResourceCalendarLeaves_company',
                                blank=True, null=True)
    calendar = models.ForeignKey(ResourceCalendar, models.DO_NOTHING, related_name='ResourceCalendarLeaves_calendar',
                                 blank=True, null=True)
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
    resource = models.ForeignKey('ResourceResource', models.DO_NOTHING, related_name='ResourceCalendarLeaves_resource',
                                 blank=True, null=True)
    time_type = models.CharField(max_length=1000, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, related_name='ResourceCalendarLeaves_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, related_name='ResourceCalendarLeaves_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resource_calendar_leaves'


class ResourceResource(models.Model):
    name = models.CharField(max_length=1000)
    active = models.BooleanField(blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, related_name='ResourceResource_company', blank=True,
                                null=True)
    resource_type = models.CharField(max_length=1000)
    user = models.ForeignKey(ResUsers, models.DO_NOTHING, related_name='ResourceResource_user', blank=True, null=True)
    time_efficiency = models.FloatField()
    calendar = models.ForeignKey(ResourceCalendar, models.DO_NOTHING)
    tz = models.CharField(max_length=1000)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, related_name='ResourceResource_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, related_name='ResourceResource_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resource_resource'


class ResourceTest(models.Model):
    name = models.CharField(max_length=1000, blank=True, null=True)
    resource = models.ForeignKey(ResourceResource, models.DO_NOTHING)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, related_name='ResourceTest_company', blank=True,
                                null=True)
    resource_calendar = models.ForeignKey(ResourceCalendar, models.DO_NOTHING,
                                          related_name='ResourceTest_resource_calendar', blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, related_name='ResourceTest_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, related_name='ResourceTest_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resource_test'


class RuleGroupRel(models.Model):
    rule_group = models.ForeignKey(IrRule, models.DO_NOTHING)
    group = models.ForeignKey(ResGroups, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'rule_group_rel'
        unique_together = (('rule_group', 'group'),)


class SmsSendSms(models.Model):
    recipients = models.CharField(max_length=1000)
    message = models.TextField()
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, related_name='SmsSendSms_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, related_name='SmsSendSms_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sms_send_sms'


class SnailmailLetter(models.Model):
    user = models.ForeignKey(ResUsers, models.DO_NOTHING, related_name='SnailmailLetter_user', blank=True, null=True)
    model = models.CharField(max_length=1000)
    res_id = models.IntegerField()
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    report_template = models.ForeignKey(IrActReportXml, models.DO_NOTHING,
                                        related_name='SnailmailLetter_report_template', db_column='report_template',
                                        blank=True, null=True)
    attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING, related_name='SnailmailLetter_attachment',
                                   blank=True, null=True)
    color = models.BooleanField(blank=True, null=True)
    duplex = models.BooleanField(blank=True, null=True)
    state = models.CharField(max_length=1000, blank=True, null=True)
    info_msg = models.CharField(max_length=1000, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, related_name='SnailmailLetter_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, related_name='SnailmailLetter_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'snailmail_letter'


class TeamFavoriteUserRel(models.Model):
    team = models.ForeignKey(CrmTeam, models.DO_NOTHING)
    user = models.ForeignKey(ResUsers, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'team_favorite_user_rel'
        unique_together = (('team', 'user'),)


class UtmCampaign(models.Model):
    name = models.CharField(max_length=1000)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, related_name='UtmCampaign_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, related_name='UtmCampaign_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utm_campaign'


class UtmMedium(models.Model):
    name = models.CharField(max_length=1000)
    active = models.BooleanField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, related_name='UtmMedium_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, related_name='UtmMedium_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utm_medium'


class UtmSource(models.Model):
    name = models.CharField(max_length=1000)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, related_name='UtmSource_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, related_name='UtmSource_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utm_source'


class WebEditorConverterTest(models.Model):
    char = models.CharField(max_length=1000, blank=True, null=True)
    integer = models.IntegerField(blank=True, null=True)
    float = models.FloatField(blank=True, null=True)
    numeric = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    many2one = models.ForeignKey('WebEditorConverterTestSub', models.DO_NOTHING,
                                 related_name='WebEditorConverterTest_many2one',
                                 db_column='many2one', blank=True, null=True)
    binary = models.BinaryField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)
    selection = models.IntegerField(blank=True, null=True)
    selection_str = models.CharField(max_length=1000, blank=True, null=True)
    html = models.TextField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, related_name='WebEditorConverterTest_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, related_name='WebEditorConverterTest_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_editor_converter_test'


class WebEditorConverterTestSub(models.Model):
    name = models.CharField(max_length=1000, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, related_name='WebEditorConverterTestSub_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, related_name='WebEditorConverterTestSub_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_editor_converter_test_sub'


class WebTourTour(models.Model):
    name = models.CharField(max_length=1000)
    user = models.ForeignKey(ResUsers, models.DO_NOTHING, related_name='WebTourTour_user', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_tour_tour'


class WizardIrModelMenuCreate(models.Model):
    menu = models.ForeignKey(IrUiMenu, models.DO_NOTHING)
    name = models.CharField(max_length=1000)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, related_name='WizardIrModelMenuCreate_create_uid',
                                   db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, related_name='WizardIrModelMenuCreate_write_uid',
                                  db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wizard_ir_model_menu_create'
